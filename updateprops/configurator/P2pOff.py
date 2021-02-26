from .SinglePropertyAbstract import SinglePropertyAbstract


class P2pOff(SinglePropertyAbstract):
    def __init__(self):
        super().__init__("LiqidNamespace.displayP2pControls = false;", 'none')
