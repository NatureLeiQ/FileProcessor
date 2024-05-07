from enum import Enum


class TraverseStrategyActionModelEnum(Enum):
    """
    全部满足、满足其中一个、必须满足某几个
    """
    FULL_SATISFACTION = 1
    SATISFACTION_AT_LAST_ONE = 2
    FULL_SATISFACTION_AND_EXCLUDE = 3
