from exception.error import LiqidError


class TomcatShutDownError(LiqidError):
    pass


class TomcatStartUpError(LiqidError):
    pass


class TomcatCleanDirError(LiqidError):
    pass

