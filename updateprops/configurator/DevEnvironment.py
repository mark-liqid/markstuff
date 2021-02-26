from .SinglePropertyAbstract import SinglePropertyAbstract


class DevEnvironment(SinglePropertyAbstract):
    def __init__(self):
        super().__init__("LiqidNamespace.environment = 'dev';", 'none')
