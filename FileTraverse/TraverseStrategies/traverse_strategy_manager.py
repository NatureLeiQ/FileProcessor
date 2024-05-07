from Expections.strategy_action_not_match_exception import StrategyActionNotMatchException
from ..TraverseStrategies.traverse_strategy_action_model_enum import TraverseStrategyActionModelEnum


class TraverseStrategyManager:

    def __init__(self, strategies, strategies_action_model_enum, exclude_strategies):
        """
        策略管理器:
        :param strategies: 遍历策略
        :param strategies_action_model_enum 策略生效模式，例如：全部满足、满足其中一个、某一个必须满足某几个
        :param exclude_strategies 排除的策略，用于[SATISFACTION_AND_EXCLUDE]这种情况，相当于被排除部分的策略
        """
        self.strategies = strategies
        self.strategies_action_model_enum = strategies_action_model_enum
        self.exclude_strategies = exclude_strategies
        self.file_path = None

    def set_current_file(self, file_path):
        self.file_path = file_path

    def should_process(self):
        if self.file_path is None:
            raise FileNotFoundError("遍历文件不存在")
        if TraverseStrategyActionModelEnum.FULL_SATISFACTION == self.strategies_action_model_enum:
            # 全部满足模式
            return self._full_satisfaction_strategy()
        if TraverseStrategyActionModelEnum.SATISFACTION_AT_LAST_ONE == self.strategies_action_model_enum:
            # 至少一个满足模式
            return self._satisfaction_at_last_one_strategy()
        if TraverseStrategyActionModelEnum.FULL_SATISFACTION_AND_EXCLUDE == self.strategies_action_model_enum:
            # 全满足+排除策略有一个不满足就排除
            return self._full_satisfaction_and_exclude_strategy()
        raise StrategyActionNotMatchException("不存在的策略生效模式")

    def _full_satisfaction_strategy(self):
        """
        全部满足策略，需要通过全部策略的检查才能返回true
        :return:
        """
        for strategy in self.strategies:
            if not strategy.can_traverse(self.file_path):
                return False
        return True

    def _satisfaction_at_last_one_strategy(self):
        """
        满足其中一个策略即可
        :return:
        """
        for strategy in self.strategies:
            if strategy.can_traverse(self.file_path):
                return True

        return False

    def _full_satisfaction_and_exclude_strategy(self):
        """
        策略全部满足，并且有一个排除策略满足就排除，否则留下
        :return:
        """
        for strategy in self.exclude_strategies:
            if strategy.can_traverse(self.file_path):
                return True

        return self._full_satisfaction_strategy()
