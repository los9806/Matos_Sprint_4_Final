import unittest
from Cinos_API.ice_cream import Ice_Cream

class TestIceCream(unittest.TestCase):

    def test_get_base_price(self):
        ice_cream = Ice_Cream("vanilla bean")
        self.assertEqual(ice_cream.get_base_price(), 3.00)

    def test_get_type(self):
        ice_cream = Ice_Cream("mint chocolate chip")
        self.assertEqual(ice_cream.get_type(), "mint chocolate chip")

    def test_add_fixins(self):
        ice_cream = Ice_Cream("chocolate")
        ice_cream.add_fixins("whipped cream")
        ice_cream.add_fixins("caramel sauce")
        self.assertEqual(ice_cream.get_fixins(), ["caramel sauce", "whipped cream"])
        self.assertEqual(ice_cream.get_num_fixins(), 2)

    def test_get_total_price(self):
        ice_cream = Ice_Cream("butter pecan")
        ice_cream.add_fixins("pecans")
        ice_cream.add_fixins("caramel sauce")
        self.assertAlmostEqual(ice_cream.get_total_price(), 4.50)

    def test_invalid_ice_cream(self):
        with self.assertRaises(ValueError):
            Ice_Cream("invalid flavor")

    def test_invalid_fixins(self):
        ice_cream = Ice_Cream("vanilla bean")
        with self.assertRaises(ValueError):
            ice_cream.add_fixins("invalid fixin")

if __name__ == "__main__":
    unittest.main()