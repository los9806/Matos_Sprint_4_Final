class Ice_Cream:
    """Class for Ice Cream flavors"""

    # Defined Ice Cream flavors and cost
    _iceCream_prices = {
        "mint chocolate chip": 4.00,
        "chocolate": 3.00,
        "vanilla bean": 3.00,
        "banana": 3.50,
        "butter pecan": 3.50,
        "smore": 4.00
    }

    # Defined price of additional toppings
    _fixins_prices = {
        "cherry": 0.00,
        "whipped cream": 0.00,
        "caramel sauce": 0.50,
        "chocolate sauce": 0.50,
        "storios": 1.00,
        "dig dogs": 1.00,
        "t&t": 1.00,
        "cookie dough": 1.00,
        "pecans": 0.50
    }

    # Getters and accessors for the different parts
    def __init__(self, iceCream_type):
        if iceCream_type.lower() not in self._iceCream_prices:
            raise ValueError(f"Invalid ice cream type.")
        self._type = iceCream_type.lower()
        self._fixins = set()
        self._base_price = self._iceCream_prices[self._type]

    def __str__(self):
        fixins = ", ".join(self.get_fixins()) or "None"
        return f"Ice Cream(type={self._type}, fixins={fixins}, total_price=${self.get_total_price():.2f})"

    def  get_base_price(self):
        """Accessor for the ice cream's base price"""
        return self._base_price

    def get_type(self):
        """Accessor for the ice cream type"""
        return self._type

    def add_fixins(self, fixins):
        """Method for adding fixins"""
        if fixins.lower() not in self._fixins_prices:
            raise ValueError(f"Invalid fixin")
        self._fixins.add(fixins.lower())

    def get_fixins(self):
        """Fixins Accessor"""
        return sorted(self._fixins)

    def get_num_fixins(self):
        """Method to get the number of fixins"""
        return len(self._fixins)

    def get_total_price(self):
        """Method to calculate the total price of ice cream and fixins"""
        fixins_cost = sum(self._fixins_prices[fixins] for fixins in self._fixins)
        return self._base_price + fixins_cost
    
    