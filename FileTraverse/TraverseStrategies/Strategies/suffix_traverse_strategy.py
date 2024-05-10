import os

from FileTraverse.TraverseStrategies.abstract_traverse_strategy import AbstractTraverserStrategy


class SuffixTraverseStrategy(AbstractTraverserStrategy):
    def __init__(self, suffix):
        """
        后缀匹配.suffix可传入单个字符串或者一个字符串列表。
        """
        super().__init__()
        self.suffix = suffix

    def can_traverse(self, file_path):
        return self.get_file_extension(file_path) == self.suffix

    @staticmethod
    def get_file_extension(file_path):
        """获取文件名的后缀（扩展名）"""
        base = os.path.basename(file_path)  # 获取文件名（不包括路径）
        return os.path.splitext(base)[1].lower()  # 返回后缀，转换为小写
