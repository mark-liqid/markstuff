from .SinglePropertyAbstract import SinglePropertyAbstract


class P2pOn(SinglePropertyAbstract):
    def __init__(self):
        super().__init__("LiqidNamespace.displayP2pControls = true;", 'none')
