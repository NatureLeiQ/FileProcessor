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
        """
         case里面每个子方法，返回的True或False都代表此文件能否被处理。都按照这个角度来看
        """
        if self.file_path is None:
            raise FileNotFoundError("遍历文件不存在")
        match self.strategies_action_model_enum:
            case TraverseStrategyActionModelEnum.FULL_SATISFACTION:
                # 满足全部策略： 是
                return self._full_satisfaction_strategy()
            case TraverseStrategyActionModelEnum.FULL_EXCLUDE:
                # 满足全部排除策略才能排除 ： 非
                return self._full_exclude_strategy()
            case TraverseStrategyActionModelEnum.SATISFACTION_AT_LAST_ONE:
                # 至少满足一个策略： 部分是
                return self._satisfaction_at_last_one_strategy()
            case TraverseStrategyActionModelEnum.EXCLUDE_AT_LAST_ONE:
                # 至少满足一个排除策略就被排除 ： 部分非
                return self._exclude_at_last_one_strategy()
            case TraverseStrategyActionModelEnum.FULL_SATISFACTION_AND_EXCLUDE:
                # 满足全部策略且不满足所有排除策略 ： 是+非
                return self._full_satisfaction_and_exclude_strategy()
            case TraverseStrategyActionModelEnum.AT_LAST_ONE_SATISFACTION_AND_EXCLUDE:
                # 至少满足一个策略且不满足所有排除策略 部分是+非
                return self._at_last_one_satisfaction_and_exclude_strategy()
            case TraverseStrategyActionModelEnum.FULL_SATISFACTION_AND_EXCLUDE_AT_LAST_ONE:
                # 策略全部满足且必须全部不满足排除策略：是+部分非
                return self._full_satisfaction_and_exclude_at_last_one()
            case TraverseStrategyActionModelEnum.AT_LAST_ONE_SATISFACTION_AND_EXCLUDE_AT_LAST_ONE:
                # 至少满足一个策略且如果排除策略不是全部满足就返回True。EXCLUDE_AT_LAST_ONE意味着有一个排除策略满足就返回False ： 部分是+部分非
                return self._at_last_one_satisfaction_and_exclude_at_last_one_strategy()

        raise StrategyActionNotMatchException("不存在的策略生效模式")

    def _full_satisfaction_strategy(self):
        """
        全部满足策略，需要通过全部策略的检查才能返回true：是
        :return:
        """
        for strategy in self.strategies:
            if not strategy.can_traverse(self.file_path):
                return False
        return True

    def _satisfaction_at_last_one_strategy(self):
        """
        满足其中一个策略即可: 部分是
        :return:
        """
        for strategy in self.strategies:
            if strategy.can_traverse(self.file_path):
                return True

        return False

    def _full_exclude_strategy(self):
        """
        满足全部排除策略才能排除：传入的普通策略无效，只有排除策略生效：非
        :return  文件可否被处理这个角度
        """
        for exclude_strategy in self.exclude_strategies:
            if not exclude_strategy.can_traverse(self.file_path):
                # 某个排除条件不满足，说明不能被排除,文件能被处理，返回true
                return True
            return False

    def _exclude_at_last_one_strategy(self):
        for exclude_strategy in self.exclude_strategies:
            if exclude_strategy.can_traverse(self.file_path):
                # 至少有一个排除策略满足，则说明需要排除掉,返回False 表示文件不可被处理
                return False
            return True

    def _full_satisfaction_and_exclude_strategy(self):
        return self._full_satisfaction_strategy() and self._full_exclude_strategy()

    def _at_last_one_satisfaction_and_exclude_strategy(self):
        return self._satisfaction_at_last_one_strategy() and self._full_exclude_strategy()

    def _full_satisfaction_and_exclude_at_last_one(self):
        return self._full_satisfaction_strategy() and self._exclude_at_last_one_strategy()

    def _at_last_one_satisfaction_and_exclude_at_last_one_strategy(self):
        return self._satisfaction_at_last_one_strategy() and self._exclude_at_last_one_strategy()


