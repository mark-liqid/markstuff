import unittest
from configurator.SinglePropertyAbstract import SinglePropertyAbstract


class TestSinglePropertyAbstract(unittest.TestCase):

    def setUp(self):
        self._ui_vlaue = 'uivalue = 192.168.1.11'
        self._api_value = 'api_value = 192.168.1.11'
        self._singlepropertyabstract = SinglePropertyAbstract(self._ui_vlaue, self._api_value)

    def test_get_ui_value(self):
        self.assertEqual(self._singlepropertyabstract.get_ui_value(), self._ui_vlaue)

    def test_get_api_value(self):
        self.assertEqual(self._singlepropertyabstract.get_api_value(), self._api_value)


if __name__ == '__main__':
    unittest.main()
