import unittest
from warmanager.WarLocator import WarLocator


class TestWarLocator(unittest.TestCase):

    def setUp(self):
        self._warlocator = WarLocator()

    def test_set_get_orig_war_dir(self):
        dir = '/test/directory'
        self._warlocator.set_orig_war_dir(dir)
        self.assertEqual(self._warlocator.get_orig_war_dir(), dir)

    def test_get_temp_war_dir(self):
        dir = '/tmp'
        self.assertEqual(self._warlocator.get_temp_war_dir(), dir)

    def test_get_dirs(self):
        orig_dir = '/test/directory'
        temp_dir = '/tmp'
        dirs = [orig_dir, temp_dir]
        self._warlocator.set_orig_war_dir(orig_dir)
        self.assertEqual(self._warlocator.get_dirs(), dirs)


if __name__ == '__main__':
    unittest.main()
