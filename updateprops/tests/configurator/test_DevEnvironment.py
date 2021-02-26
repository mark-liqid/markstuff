import unittest
from configurator.DevEnvironment import DevEnvironment


class TestDevEnvironment(unittest.TestCase):

    def test_dev_environment(self):
        dev = DevEnvironment()
        self.assertEqual(dev.get_ui_value(), "LiqidNamespace.environment = 'dev';")
        self.assertEqual(dev.get_api_value(), "none")


if __name__ == '__main__':
    unittest.main()
