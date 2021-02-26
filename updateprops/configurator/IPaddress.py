from .SinglePropertyAbstract import SinglePropertyAbstract


class IpAdress(SinglePropertyAbstract):
    def __init__(self, ip_value):
        # self.setUiValue( ui_value )
        # self.setApiValue( api_value )
        super().__init__(self.build_ui_value(ip_value), self.build_api_value(ip_value))

    @staticmethod
    def build_ui_value(ip_value):
        value = 'LiqidNamespace.server = \'' + ip_value + '\';'
        return value

    @staticmethod
    def build_api_value(ip_value):
        value = 'linux.management.node.address=' + ip_value
        return value
