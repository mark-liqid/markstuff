import unittest
import re
from configurator.FileUpdater import FileUpdater


class TestFileUpdater(unittest.TestCase):

    def setUp(self):
        pass

    def test_ui_ip_regex(self):
        self.assertTrue(re.match(FileUpdater('/test').ui_ip_regex(), 'LiqidNamespace.server = "192.168.1.11";'))

    def test_ui_env_regex(self):
        self.assertTrue(re.match(FileUpdater('/test').ui_env_regex(), "LiqidNamespace.environment = 'prod';"))
        self.assertTrue(re.match(FileUpdater('/test').ui_env_regex(), "LiqidNamespace.environment = 'dev';"))

    def test_ui_sec_regex(self):
        self.assertTrue(re.match(FileUpdater('/test').ui_sec_regex(), 'LiqidNamespace.security = "off";'))
        self.assertTrue(re.match(FileUpdater('/test').ui_sec_regex(), 'LiqidNamespace.security = "on";'))

    def test_ui_p2p_regex(self):
        self.assertTrue(re.match(FileUpdater('/test').ui_p2p_regex(), 'LiqidNamespace.displayP2pControls = true;'))
        self.assertTrue(re.match(FileUpdater('/test').ui_p2p_regex(), 'LiqidNamespace.displayP2pControls = false;'))

    def test_api_ip_regex(self):
        self.assertTrue(re.match(FileUpdater('/test').api_ip_regex(), 'linux.management.node.address=192.168.1.11'))

    def test_api_sec_regex(self):
        self.assertTrue(re.match(FileUpdater('/test').api_sec_regex(), 'liqid.security.mode=off'))
        self.assertTrue(re.match(FileUpdater('/test').api_sec_regex(), 'liqid.security.mode=on'))


if __name__ == '__main__':
    unittest.main()
