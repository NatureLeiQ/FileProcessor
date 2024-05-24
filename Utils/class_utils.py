import warnings
from functools import wraps


def deprecated(func):
    @wraps(func)
    def new_func(*args, **kwargs):
        warnings.warn(f"{func.__name__} is deprecated and may be removed in future versions.",
                      DeprecationWarning, stacklevel=2)
        return func(*args, **kwargs)

    return new_func
