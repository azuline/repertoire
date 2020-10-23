from functools import wraps
from typing import Any, Callable, Union

from backend.enums import GraphQLError
from backend.graphql.types.error import Error


def require_auth(func: Callable) -> Callable:
    """
    A decorator that enforces authentication on a GraphQL resolver. If
    ``info.context.user`` is ``None``, then ``None`` will be returned from the resolver.

    :param func: The function to wrap.
    """

    @wraps(func)
    def wrapper(obj, info, **kwargs) -> Union[Any, GraphQLError]:
        if not info.context.user:
            return Error(
                error=GraphQLError.NOT_AUTHENTICATED,
                message="Please authenticate ^.~",
            )

        return func(obj, info, **kwargs)

    return wrapper


def resolve_result(success_type: str) -> Callable:
    """
    Returns a resolver function for ``*Result`` union types. Returns "Error" if the
    returned type is an error, otherwise returns ``success_type``.

    :param success_type: The name of the success/non-error type.
    :return: A resolver function for ``{success_type}Result``..
    """

    def resolver(obj, _info, _return_type) -> str:
        if isinstance(obj, Error):
            return "Error"

        return success_type

    return resolver
