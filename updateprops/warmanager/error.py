from exception.error import LiqidError


class WarMoverError(LiqidError):
    pass


class WarExpandError(LiqidError):
    pass


class WarCompressError(LiqidError):
    pass


class WarCleanupError(LiqidError):
    pass
