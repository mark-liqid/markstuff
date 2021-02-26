import unittest
from configurator.P2pOff import P2pOff


class TestP2pOff(unittest.TestCase):

    def test_p2p_off(self):
        p2p = P2pOff()
        self.assertEqual(p2p.get_ui_value(), "LiqidNamespace.displayP2pControls = false;")
        self.assertEqual(p2p.get_api_value(), "none")


if __name__ == '__main__':
    unittest.main()
