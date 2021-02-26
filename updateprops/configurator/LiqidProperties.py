import re
import configurator.error as error
from .DevEnvironment import DevEnvironment
from .ProdEnvironment import ProdEnvironment
from .SecurityOn import SecurityOn
from .SecurityOff import SecurityOff
from .P2pOn import P2pOn
from .P2pOff import P2pOff
from .IPaddress import IpAdress
from utils.message.Message import Message


class LiqidProperties(object):
    def __init__(self):
        self._ui_props = {}
        self._api_props = {}

    def get_ui_props(self):
        return self._ui_props

    def get_api_props(self):
        return self._api_props

    # ip
    def collect_ip_input(self):
        while True:
            ipinput = input("IP Address? ")
            pattern = re.compile("[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+")
            if not pattern.match(ipinput):
                Message("Invalid IP")
                continue
            else:
                self.set_ip_prop(ipinput)
                break

    def set_ip_prop(self, value):
        ip = IpAdress(value)
        self._ui_props['ip'] = ip.get_ui_value()
        self._api_props['ip'] = ip.get_api_value()

    # environment
    def collect_environment_input(self):
        while True:
            envinput = input("Environment? (dev/prod) ")
            if envinput not in ['dev', 'prod']:
                Message('Invalid Input. Use "dev" or "prod" ')
                continue
            else:
                self.set_env_prop(envinput)
                break

    def set_env_prop(self, value):
        env = None
        if value == 'dev':
            env = DevEnvironment()
        elif value == 'prod':
            env = ProdEnvironment()
        else:
            raise error.EnvPropertyError('Invalid -env value! (dev/prod)')

        self._ui_props['env'] = env.get_ui_value()
        self._api_props['env'] = env.get_api_value()

    # security
    def collect_security_input(self):
        while True:
            secinput = input("Secure mode? (on/off) ")
            if secinput not in ['on', 'off']:
                Message('Invalid Input. Use "on" or "off" ')
            else:
                self.set_sec_prop(secinput)
                break

    def set_sec_prop(self, value):
        sec = None
        if value == 'on':
            sec = SecurityOn()
        elif value == 'off':
            sec = SecurityOff()
        else:
            raise error.SecPropertyError('Invalid -sec value! (on/off)')

        self._ui_props['sec'] = sec.get_ui_value()
        self._api_props['sec'] = sec.get_api_value()

    # p2p
    def collect_p2p_input(self):
        while True:
            p2pinput = input("P2P in UI? (on/off) ")
            if p2pinput not in ['on', 'off']:
                Message('Invalid Input. Use "on" or "off" ')
            else:
                self.set_p2p_prop(p2pinput)
                break

    def set_p2p_prop(self, value):
        p2p = None
        if value == 'on':
            p2p = P2pOn()
        elif value == 'off':
            p2p = P2pOff()
        else:
            raise error.P2pPropertyError('Invalid -p2p value! (on/off)')

        self._ui_props['p2p'] = p2p.get_ui_value()
        self._api_props['p2p'] = p2p.get_api_value()
