import unittest
from configurator.SecurityOff import SecurityOff


class TestSecurityOff(unittest.TestCase):

    def test_security_off(self):
        sec = SecurityOff()
        self.assertEqual(sec.get_ui_value(), "LiqidNamespace.security = 'off';")
        self.assertEqual(sec.get_api_value(), "liqid.security.mode=off")


if __name__ == '__main__':
    unittest.main()
