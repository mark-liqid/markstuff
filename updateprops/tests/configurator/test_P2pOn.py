import unittest
from configurator.P2pOn import P2pOn


class TestP2pOn(unittest.TestCase):

    def test_p2p_on(self):
        p2p = P2pOn()
        self.assertEqual(p2p.get_ui_value(), "LiqidNamespace.displayP2pControls = true;")
        self.assertEqual(p2p.get_api_value(), "none")


if __name__ == '__main__':
    unittest.main()
