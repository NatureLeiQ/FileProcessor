from enum import Enum


class TraverseStrategyActionModelEnum(Enum):
    """
    全部满足、满足其中一个、必须满足某几个
    """
    # 满足全部策略 ： 是
    FULL_SATISFACTION = 1
    # 满足全部排除策略才能排除 ： 非
    FULL_EXCLUDE = 2
    # 至少满足一个策略： 部分是
    SATISFACTION_AT_LAST_ONE = 3
    # 至少满足一个排除策略就被排除 ： 部分非
    EXCLUDE_AT_LAST_ONE = 4
    # 满足全部策略且不满足所有排除策略 ： 是+非
    FULL_SATISFACTION_AND_EXCLUDE = 5
    # 至少满足一个策略且不满足所有排除策略 部分是+非
    AT_LAST_ONE_SATISFACTION_AND_EXCLUDE = 6
    # 策略全部满足且必须全部不满足排除策略：是+部分非
    FULL_SATISFACTION_AND_EXCLUDE_AT_LAST_ONE = 7
    # 至少满足一个策略且如果排除策略不是全部满足就返回True。EXCLUDE_AT_LAST_ONE意味着有一个排除策略满足就返回False ： 部分是+部分非
    AT_LAST_ONE_SATISFACTION_AND_EXCLUDE_AT_LAST_ONE = 8
