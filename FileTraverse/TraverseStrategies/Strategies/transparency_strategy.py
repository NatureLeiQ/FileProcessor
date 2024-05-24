from FileTraverse.TraverseStrategies.abstract_traverse_strategy import AbstractTraverserStrategy


class TransparencyStrategy(AbstractTraverserStrategy):
    def __init__(self):
        super().__init__()

    """
     透明策略，表示确定的文件，不需要任何策略来筛选遍历.当策略传None的时候会创建一个默认的此策略，这个策略目的是为了维持系统的健壮性
    """

    def can_traverse(self, file_path):
        return True
