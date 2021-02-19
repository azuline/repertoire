from functools import wraps
from typing import Callable


def transaction(func: Callable) -> Callable:
    """
    A decorator that adds a post-commit on a GraphQL mutation. After a mutation
    finishes, this decorator will make sure that changes are committed to the database.

    :param func: The mutation resolver to wrap.
    """

    @wraps(func)
    def wrapper(obj, info, **kwargs):
        rval = func(obj, info, **kwargs)
        info.context.db.connection.commit()
        return rval

    return wrapper
