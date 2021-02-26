import unittest
from configurator.ProdEnvironment import ProdEnvironment


class TestProdEnvironment(unittest.TestCase):

    def test_prod_environment(self):
        prod = ProdEnvironment()
        self.assertEqual(prod.get_ui_value(), "LiqidNamespace.environment = 'prod';")
        self.assertEqual(prod.get_api_value(), "none")


if __name__ == '__main__':
    unittest.main()
