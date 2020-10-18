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
