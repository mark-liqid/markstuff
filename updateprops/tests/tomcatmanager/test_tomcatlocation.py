import unittest
from tomcatmanager.tomcatlocation import get_tomcat_location
from tomcatmanager.tomcatlocation import get_catalina_location


class TestTomcatInput(unittest.TestCase):

    def test_get_tomcat_dir(self):
        self.assertEqual(get_tomcat_location(), '/opt/tomcat/current/')

    def test_get_catalina_dir(self):
        self.assertEqual(get_catalina_location(), '/opt/tomcat/current/bin/')


if __name__ == '__main__':
    unittest.main()
