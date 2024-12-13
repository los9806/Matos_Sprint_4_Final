import unittest
from Cinos_API.drink import Drink
from Cinos_API.food import Food
from Cinos_API.ice_cream import Ice_Cream
from Cinos_API.cinos_order import Order


class TestOrder(unittest.TestCase):

    def setUp(self):
        """Set up a common Order instance for tests."""
        self.order = Order()

    def test_add_items_and_get_total(self):
        # Add a Food item
        nachos = Food("nachos")
        nachos.add_topping("chili")
        nachos.add_topping("mustard")
        self.order.add_item(nachos)

        # Add a Drink item
        sbrite = Drink("medium")
        sbrite.add_flavor("lemon")
        sbrite.add_flavor("mint")
        self.order.add_item(sbrite)

        # Add an Ice Cream item
        ice_cream = Ice_Cream("chocolate")
        ice_cream.add_fixins("whipped cream")
        ice_cream.add_fixins("caramel sauce")
        self.order.add_item(ice_cream)

        # Verify the total
        expected_total = nachos.get_total_price() + sbrite.get_total() + ice_cream.get_total_price()
        self.assertAlmostEqual(self.order.get_total(), expected_total, places=2)

        # Verify the total with tax
        expected_total_with_tax = expected_total * (1 + Order._tax_rate)
        self.assertAlmostEqual(self.order.get_tax(), expected_total_with_tax, places=2)

    def test_receipt_output(self):
        # Add items to the order
        nachos = Food("nachos")
        nachos.add_topping("nacho cheese")
        self.order.add_item(nachos)

        pokecola = Drink("small")
        pokecola.set_base("sbrite")
        self.order.add_item(pokecola)

        ice_cream = Ice_Cream("vanilla bean")
        self.order.add_item(ice_cream)

        # Generate receipt
        receipt = self.order.get_receipt()

        # Check receipt content
        self.assertIn("nachos", receipt)
        self.assertIn("nacho cheese", receipt)
        self.assertIn("sbrite", receipt)
        self.assertIn("vanilla bean", receipt)
        self.assertIn(f"Total (with tax): ${self.order.get_tax():.2f}", receipt)

    def test_remove_item(self):
        # Add multiple items
        food = Food("corndog")
        drink = Drink("small")
        ice_cream = Ice_Cream("butter pecan")
        self.order.add_item(food)
        self.order.add_item(drink)
        self.order.add_item(ice_cream)

        # Remove the second item (drink)
        self.order.remove_item(1)

        # Verify the number of items
        self.assertEqual(len(self.order.get_items()), 2)

        # Verify remaining items
        self.assertEqual(self.order.get_items()[0], food)
        self.assertEqual(self.order.get_items()[1], ice_cream)

    def test_invalid_item_removal(self):
        with self.assertRaises(IndexError):
            self.order.remove_item(0)  # Empty order

        food = Food("tater tots")
        self.order.add_item(food)
        with self.assertRaises(IndexError):
            self.order.remove_item(5)  # Out of range


if __name__ == "__main__":
    unittest.main()

