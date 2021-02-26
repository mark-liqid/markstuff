from .SinglePropertyAbstract import SinglePropertyAbstract


class SecurityOff(SinglePropertyAbstract):
    def __init__(self):
        super().__init__("LiqidNamespace.security = 'off';", "liqid.security.mode=off")
