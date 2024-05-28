from FileTraverse.TraverseStrategies.abstract_traverse_strategy import AbstractTraverserStrategy
from Utils.file_utils import resolve_file_path


class FileNameStrategy(AbstractTraverserStrategy):
    """
    文件名策略
    """

    def __init__(self, match_names, part_match=False, include=True):
        super().__init__()
        if not isinstance(match_names, list):
            match_names = [match_names]
        self.match_names = match_names
        self.part_match = part_match  # 部分匹配。默认为完全匹配
        self.include = include  # include=True表示只检查这个包下面的，include=False表示排除这个包下面的

    def can_traverse(self, file_path):
        resolved_file_path = resolve_file_path(file_path)
        file_name = resolved_file_path["file_name"]
        for name in self.match_names:
            if self.include:
                if self.part_match:  # 包含
                    if name in file_name:
                        return True
                else:
                    if name == file_name:
                        return True
            else:
                if self.part_match:
                    if name in file_name:
                        return False
                else:
                    if name == file_name:
                        return False

        if self.include:
            return False
        else:
            return True
