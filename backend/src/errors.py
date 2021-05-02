from typing import Any, Optional


class BackendError(Exception):
    pass


class CliError(BackendError):
    pass


class InvalidConfig(BackendError):
    pass


class LibError(BackendError):
    #: The error message.
    message: Optional[str]

    def __init__(self, message: Optional[str] = None, *args, **kwargs):
        self.message = message
        super().__init__(message, *args, **kwargs)  # type: ignore


class InvalidNickname(LibError):
    """
    This error does not accept a message as a part of its constructor.

    The message is static to the exception.
    """

    def __init__(self, *args, **kwargs):
        self.message = "Invalid nickname. Nicknames must be less than 24 characters."
        super().__init__(self.message, *args, **kwargs)


class TokenGenerationFailure(LibError):
    pass


class CodeGenerationFailure(LibError):
    pass


class InvalidCollectionType(LibError):
    pass


class InvalidPlaylistType(LibError):
    pass


class InvalidArgument(LibError):
    pass


class Immutable(LibError):
    pass


class NotFound(LibError):
    pass


class Duplicate(LibError):
    #: The duplicate entity.
    entity: Any

    def __init__(self, message: str = None, entity: Any = None, *args, **kwargs):
        self.entity = entity
        super().__init__(message, entity, *args, **kwargs)


class AlreadyExists(LibError):
    pass


class DoesNotExist(LibError):
    pass


class ParseError(LibError):
    pass


class InvalidImage(LibError):
    pass
