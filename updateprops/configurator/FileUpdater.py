import re
import fileinput


class FileUpdater(object):
    def __init__(self, file_path):
        self._file_path = file_path

    def do_ui_updates(self, values):
        ipvalue = values['ip']
        envvalue = values['env']
        secvalue = values['sec']
        p2pvalue = values['p2p']

        uifile = fileinput.FileInput(self._file_path, inplace=True, backup='.bak')

        for line in uifile:
            line = re.sub(self.ui_ip_regex(), ipvalue, line.rstrip())
            line = re.sub(self.ui_env_regex(), envvalue, line.rstrip())
            line = re.sub(self.ui_sec_regex(), secvalue, line.rstrip())
            line = re.sub(self.ui_p2p_regex(), p2pvalue, line.rstrip())
            print(line)

    def do_api_updates(self, values):
        ipvalue = values['ip']
        secvalue = values['sec']

        apifile = fileinput.FileInput(self._file_path, inplace=True, backup='.bak')

        for line in apifile:
            line = re.sub(self.api_ip_regex(), ipvalue, line.rstrip())
            line = re.sub(self.api_sec_regex(), secvalue, line.rstrip())
            print(line)

    @staticmethod
    def ui_ip_regex():
        return re.compile(r"LiqidNamespace.server = ['\"][0-9]+\.[0-9]+\.[0-9]+\.[0-9]+['\"];")

    @staticmethod
    def ui_env_regex():
        return re.compile(r"LiqidNamespace\.environment = ['\"][a-z]+.*['\"];")

    @staticmethod
    def ui_sec_regex():
        return re.compile(r"LiqidNamespace\.security = ['\"][a-z]+.*['\"];")

    @staticmethod
    def ui_p2p_regex():
        return re.compile(r"LiqidNamespace\.displayP2pControls = [a-z]+;")

    @staticmethod
    def api_ip_regex():
        return re.compile(r"linux.management.node.address=[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+")

    @staticmethod
    def api_sec_regex():
        return re.compile(r"liqid.security.mode=[a-z]+")
