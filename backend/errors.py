from typing import Any


class BackendError(Exception):
    pass


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


class Duplicate(LibError):

    #: The duplicate entity.
    entity: Any

    def __init__(self, entity: Any = None):
        self.entity = entity


class AlreadyExists(LibError):
    pass


class DoesNotExist(LibError):
    pass
