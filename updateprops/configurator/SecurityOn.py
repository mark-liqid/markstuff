from .SinglePropertyAbstract import SinglePropertyAbstract


class SecurityOn(SinglePropertyAbstract):
    def __init__(self):
        super().__init__("LiqidNamespace.security = 'on';", "liqid.security.mode=on")
