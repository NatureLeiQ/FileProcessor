from FileProcessors.processor_composite import ProcessorComposite
from FileTraverse.TraverseStrategies.traverse_strategy_manager import TraverseStrategyManager
from FileTraverse.file_traverse import FileTraverse


class Dispatcher:
    def __init__(self, root_path, generate_path, strategies, strategies_action_model_enum, generators,
                 exclude_strategies=None,
                 specify_processors=None):
        """
        :param root_path: 文件扫描的根路径
        :param strategies: 文件扫描的策略
        :param strategies_action_model_enum: 策略生效模式
        :param exclude_strategies: 文件排除的策略
        :param specify_processors: 指定的文件处理器，不指定会遍历所有可执行的处理器。后期可重构，加入处理器的执行策略。类似遍历策略一样
        """
        self.root_path = root_path
        self.strategies = strategies
        self.strategies_action_model_enum = strategies_action_model_enum
        self.exclude_strategies = exclude_strategies
        self.file_traverse = self._config_file_traverse()
        self.processor_composite = ProcessorComposite(specify_processors, generators, generate_path)
        self.traverse_paths = None

    def run(self):
        self.file_traverse.traverse()
        self.traverse_paths = self.file_traverse.traverse_paths
        # 对这些路径进行processor处理操作
        # 需要一个映射吗？每个处理器的结果可能根本不同，如何保证不同的处理器能够处理到正确的内容？处理器目前来说是根据文件类型来处理的，然后处理器里面还包括不同的功能执行器，以执行不同的功能
        for traverse_path in self.traverse_paths:
            self.processor_composite.process(traverse_path)

    def _config_file_traverse(self):
        return FileTraverse(self.root_path, self._config_traverse_strategy_manager())

    def _config_traverse_strategy_manager(self):
        """
        配置策略管理器
        :return:
        """
        return TraverseStrategyManager(self.strategies, self.strategies_action_model_enum, self.exclude_strategies)
