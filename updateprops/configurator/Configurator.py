from .LiqidProperties import LiqidProperties
from .FileUpdater import FileUpdater
from .Cleanup import Cleanup
from utils.message.Message import Message


class Configurator(object):
    def __init__(self, args):
        self._liqidprops = LiqidProperties()

        try:
            ip = args.index('-ip') + 1
            env = args.index('-env') + 1
            sec = args.index('-sec') + 1
            p2p = args.index('-p2p') + 1
            self.run_w_inputs(args[ip], args[env], args[sec], args[p2p])
        except ValueError:
            self.run_wo_inputs()

    def run_wo_inputs(self):
        self.collect_inputs()
        self.do_ui_update()
        self.do_api_update()
        self.do_cleanup()
        self.complete()

    def run_w_inputs(self, ip, env, sec, p2p):
        self._liqidprops.set_ip_prop(ip)
        self._liqidprops.set_env_prop(env)
        self._liqidprops.set_sec_prop(sec)
        self._liqidprops.set_p2p_prop(p2p)
        self.do_ui_update()
        self.do_api_update()
        self.do_cleanup()
        self.complete()

    def collect_inputs(self):
        self._liqidprops.collect_ip_input()
        self._liqidprops.collect_environment_input()
        self._liqidprops.collect_security_input()
        self._liqidprops.collect_p2p_input()

    def do_ui_update(self):
        uiupdate = FileUpdater('/tmp/unziptemp/scripts/properties.js')
        uiupdate.do_ui_updates(self._liqidprops.get_ui_props())

    def do_api_update(self):
        apiupdate = FileUpdater('/tmp/unziptemp/WEB-INF/classes/liqidui.properties')
        apiupdate.do_api_updates(self._liqidprops.get_api_props())

    def do_cleanup(self):
        Cleanup('/tmp/unziptemp/scripts/properties.js').clean()
        Cleanup('/tmp/unziptemp/WEB-INF/classes/liqidui.properties').clean()

    @staticmethod
    def complete():
        Message('Files updated')
