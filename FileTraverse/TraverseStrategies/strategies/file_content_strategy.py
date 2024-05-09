from FileTraverse.TraverseStrategies.abstract_traverse_strategy import AbstractTraverserStrategy


class FileContentStrategy(AbstractTraverserStrategy):
    """
    文件内容策略，对文件的内容进行检索，最终可生成
    """
    def __init__(self):
        pass

    def can_traverse(self, file_path):
        pass
