class Food:
    """Class for food items"""

    # Defined food and price of items
    _food_prices = {
        "hotdog": 2.30,
        "corndog": 2.00,
        "ice cream": 3.00,
        "onion rings": 1.75,
        "french fries": 1.50,
        "tater tots": 1.70,
        "nachos": 1.90
    }

    # Defined price of additional toppings
    _topping_prices = {
        "cherry": 0.00,
        "whipped cream": 0.00,
        "caramel sauce": 0.50,
        "chocolate sauce": 0.50,
        "nacho cheese": 0.30,
        "chili": 0.60,
        "bacon bits": 0.30,
        "ketchup": 0.00,
        "mustard": 0.00
    }

    # Getters and accessors for the different parts
    def __init__(self, food_type):
        if food_type.lower() not in self._food_prices:
            raise ValueError(f"Invalid food type.")
        self._type = food_type.lower()
        self._toppings = set()
        self._base_price = self._food_prices[self._type]

    def __str__(self):
        toppings = ", ".join(self.get_toppings()) or "None"
        return f"Food(type={self.get_type()}, toppings={toppings}, total_price=${self.get_total_price():.2f})"

    def  get_base_price(self):
        """Accessor for the base price of the food"""
        return self._base_price

    def get_type(self):
        """Accessor for the food type"""
        return self._type

    def add_topping(self, topping):
        """Method for adding toppings"""
        if topping.lower() not in self._topping_prices:
            raise ValueError(f"Invalid topping")
        self._toppings.add(topping.lower())

    def get_toppings(self):
        """Accessor for the toppings"""
        return list(self._toppings)

    def get_num_toppings(self):
        """Method to get the number of toppings"""
        return len(self._toppings)

    def get_total_price(self):
        """Method to calculate the total food price"""
        toppings_cost = sum(self._topping_prices[topping] for topping in self._toppings)
        return self._base_price + toppings_cost
    
    