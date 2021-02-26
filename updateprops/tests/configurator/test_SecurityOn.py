import unittest
from configurator.SecurityOn import SecurityOn


class TestSecurityOn(unittest.TestCase):

    def test_security_on(self):
        sec = SecurityOn()
        self.assertEqual(sec.get_ui_value(), "LiqidNamespace.security = 'on';")
        self.assertEqual(sec.get_api_value(), "liqid.security.mode=on")


if __name__ == '__main__':
    unittest.main()
