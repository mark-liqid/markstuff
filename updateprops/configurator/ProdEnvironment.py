from .SinglePropertyAbstract import SinglePropertyAbstract


class ProdEnvironment(SinglePropertyAbstract):
    def __init__(self):
        super().__init__("LiqidNamespace.environment = 'prod';", 'none')
