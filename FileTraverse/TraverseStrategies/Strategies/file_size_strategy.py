import math
import os

from Expections.parameter_not_match_exception import ParameterNotMatchException
from Expections.parameter_num_exception import ParameterNumException
from FileTraverse.TraverseStrategies.abstract_traverse_strategy import AbstractTraverserStrategy
from Utils.file_unit_enums import FileUnitEnums


class FileSizeStrategy(AbstractTraverserStrategy):
    """
     文件大小策略
    """
    # pattern
    MAX_MIN = 1  # 值区间模式
    MAX_VALUE = 2  # 最大值模式。筛选文件的最大尺寸
    MIN_VALUE = 3  # 最小值模式。筛选文件的最小尺寸

    #
    def __init__(self, size, unit, *x):
        super().__init__()
        if len(x) > 1:
            raise ParameterNumException("参数数量过多，只能接收一个参数")
        if size is None:
            raise ParameterNotMatchException("文件大小参数不应为空")
        self.size = size
        self.second_param = None
        self.pattern = self._init_pattern(size, x)

        if unit is None:
            unit = FileUnitEnums.KB
        self.unit = unit
        self._check_unit(self.unit)

    def _init_pattern(self, size, x):
        if len(x) == 0:
            return FileSizeStrategy.MAX_VALUE
        else:
            self.second_param = x[0]

        if isinstance(self.second_param, bool):
            if self.second_param is True:
                return FileSizeStrategy.MAX_VALUE
            else:
                return FileSizeStrategy.MIN_VALUE
        elif isinstance(self.second_param, int):
            if size < self.second_param:
                raise ParameterNotMatchException(f"最大值{size}，不应该小于最小值{self.second_param}")
            else:
                return FileSizeStrategy.MAX_MIN
        else:
            raise ParameterNotMatchException("请检查输入参数是否规范")

    @staticmethod
    def _check_unit(unit):
        match unit:
            case FileUnitEnums.B | FileUnitEnums.KB | FileUnitEnums.MB | FileUnitEnums.GB | FileUnitEnums.TB:
                return
        raise ParameterNotMatchException(f"请检查输入的单位参数是否规范：{unit}")

    def can_traverse(self, file_path):
        file_unit_size = self._convert_byte_2_unit(file_path)
        match self.pattern:
            case FileSizeStrategy.MAX_MIN:
                return self.second_param <= file_unit_size <= self.size
            case FileSizeStrategy.MAX_VALUE:
                return file_unit_size <= self.size
            case FileSizeStrategy.MIN_VALUE:
                return file_unit_size >= self.size

    def _convert_byte_2_unit(self, file_path):
        file_stats = os.stat(file_path)
        file_size_bytes = file_stats.st_size
        if self.unit == FileUnitEnums.B:
            return file_size_bytes
        return file_size_bytes / math.pow(1024, self.unit)

