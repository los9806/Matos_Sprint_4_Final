from .drink import Drink
from .food import Food
from .ice_cream import Ice_Cream

class Order: 
    """Class to contain our order items"""

    # tax rate
    _tax_rate = 0.0725

    # Initialize the class
    def __init__(self):
        self._items = []    # Create a list as a starting point 

    def __str__(self):
        items_str = "\n".join(f"{i + 1}: {item}" for i, item in enumerate(self.get_items()))
        total_with_tax = self.get_tax()
        return f"Order:\n{items_str}\nTotal (with tax): ${total_with_tax:.2f}"

    # GETTERS for the items and total of items
    def get_items(self):
        return self._items
    
    def get_num_items(self):
        return len(self._items)

    def get_total(self):
        return sum(
            item.get_total_price() if hasattr(item, 'get_total_price') else item.get_total()
            for item in self._items
        )

    def get_tax(self):
        return self.get_total() * (1 + self._tax_rate)
    
    # Receipt Data
    def get_receipt(self):
        receipt = "Order Receipt:\n"
        for i, item in enumerate(self._items):
            if isinstance(item, Drink):
                base = item.get_base()
                flavors = ", ".join(item.get_flavors()) or "None"
                receipt += f"{i + 1}: Drink - Base: {base}, Flavors: {flavors}, Price: ${item.get_total():.2f}\n"
            elif isinstance(item, Food):
                food_type = item.get_type()
                toppings = ", ".join(item.get_toppings()) or "None"
                receipt += f"{i + 1}: Food - Type: {food_type}, Toppings: {toppings}, Price: ${item.get_total_price():.2f}\n"
            elif isinstance(item, Ice_Cream):
                ice_cream_type = item.get_type()
                fixins = ", ".join(item.get_fixins()) or "None"
                receipt += f"{i + 1}: Ice Cream - Type: {ice_cream_type}, Fixins: {fixins}, Price: ${item.get_total_price():.2f}\n"
        receipt += f"Total (with tax): ${self.get_tax():.2f}"
        return receipt

    def add_item(self, item):
        """Method for adding an item to the order"""
        if isinstance(item, (Drink, Food, Ice_Cream)):
            self._items.append(item)
        else:
            raise ValueError("Only Drink, Food, or Ice_Cream objects can be added to the order.")
        
    def remove_item(self, index):
        """Method for removing items from the order"""
        if 0 <= index < len(self._items):
            self._items.pop(index)
        else:
            raise IndexError("Invalid index. Cannot remove item.")
        