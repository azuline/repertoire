from typing import Any


class BackendError(Exception):
    def __init__(self, message=None, **kwargs):
        self.message = message
        super().__init__(message, **kwargs)


class CliError(BackendError):
    pass


class InvalidConfig(BackendError):
    pass


class LibError(BackendError):
    pass


class InvalidUsername(LibError):
    pass


class TokenGenerationFailure(LibError):
    pass


class InvalidCollectionType(LibError):
    pass


class ImmutableCollection(LibError):
    pass


class NotFound(LibError):
    pass


class Duplicate(LibError):

    #: The duplicate entity.
    entity: Any

    def __init__(self, entity: Any = None):
        self.entity = entity


class AlreadyExists(LibError):
    pass


class DoesNotExist(LibError):
    pass
