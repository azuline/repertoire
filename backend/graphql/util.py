from functools import wraps
from typing import Callable

from backend.errors import NotAuthorized


def require_auth(func: Callable) -> Callable:
    """
    A decorator that enforces authorization on a GraphQL resolver. If
    ``info.context.user`` is ``None``, then ``NotAuthorized`` will be raised.

    :param func: The function to wrap.
    """

    @wraps(func)
    def wrapper(obj, info, **kwargs):
        if not info.context.user:
            raise NotAuthorized("Invalid authorization token.")

        return func(obj, info, **kwargs)

    return wrapper
