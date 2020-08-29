class BackendError(Exception):
    pass


class CliError(BackendError):
    pass


class InvalidConfig(BackendError):
    pass
