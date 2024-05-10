from FileTraverse.TraverseStrategies.abstract_traverse_strategy import AbstractTraverserStrategy


class FileNameStrategy(AbstractTraverserStrategy):
    """
    文件名策略 TODO，文件名可以是全字匹配或者部分匹配，可分与不分大小写
    """

    def __init__(self, name):
        super().__init__()

    def can_traverse(self, file_path):
        pass
