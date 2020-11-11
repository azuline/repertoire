from functools import wraps
from typing import Callable

from src.errors import NotAuthorized


def require_auth(func: Callable) -> Callable:
    """
    A decorator that enforces authorization on a GraphQL resolver. If
    ``info.context.user`` is ``None``, then ``NotAuthorized`` will be raised.

    :param func: The GraphQL resolver to wrap.
    """

    @wraps(func)
    def wrapper(obj, info, **kwargs):
        if not info.context.user:
            raise NotAuthorized("Invalid authorization token.")

        return func(obj, info, **kwargs)

    return wrapper


def commit(func: Callable) -> Callable:
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
