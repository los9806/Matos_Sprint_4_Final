class Drink:
    """A class for drink:
    That stores a 'base' 
    And the 'flavors' that haver been added"""

    # Valid bases and flavors for all instances
    _valid_bases = {"water", "sbrite", "pokecola", "Mr. Salt", "hill fog", "leaf wine"} 
    _valid_flavors = {"lemon", "cherry", "strawberry", "mint", "blueberry", "lime"}     

    # Needed size and cost for each drink
    _size_costs = {
        "small": 1.50,
        "medium": 1.75,
        "large": 2.05,
        "mega": 2.15,
    }

    # Initializer for GETTERS:
    def __init__(self, size):       # added size
        self._base = None
        self._flavors = set()   # -> 'set()' helps avoid duplicates for flavors
        self.size = None            # set the size and cost to 0
        self._cost = 0.0 
        self.set_size(size)         # sets the cost to the appropriate size

    def __str__(self):
        flavors = ", ".join(self.get_flavors()) or "None"
        return f"Drink(base={self.get_base()}, flavors={flavors}, total_price=${self.get_total():.2f})"

    # GETTERS to grab the different aspects for the drink:
    def get_base(self):
        return self._base
    
    # returns a 'list' for usr access
    def get_flavors(self):
        return list(self._flavors) 
    
    # Keeps a tracker for number of flavors added 
    def get_num_flavors(self):      
        return len(self._flavors)
    
    # Get the total
    def get_total(self):
        return self._cost
    
    # Get the size
    def get_size(self):
        return self.size
    
    # set the base:
    def set_base(self, base):
        if base in self._valid_bases: # Validates the base
            self._base = base
        else:
            raise ValueError(f"Invalid base: {base}. Choose a different base from {self._valid_bases}.")
        
    def add_flavor(self, flavor):       
        if flavor in self._valid_flavors:
            if flavor not in self._flavors: # Only charges for 1 instance of the same flavor 
                self._cost += 0.15
            self._flavors.add(flavor)       # Checks for a valid flavor, then adds to list (helps with duplication)
        else: 
            raise ValueError(f"Invalid flavor: {flavor}. Choose a different flavor from {self._valid_flavors}.")

    # set the falvors:    
    def set_flavors(self, flavors):
        if all(flavor in self._valid_flavors for flavor in flavors):
            new_flavors = set(flavors) - self._flavors
            self._cost += 0.15 * len(new_flavors)   # adds additional cost for flavors not already added 
            self._flavors = set(flavors)
        else:
            invalid_flavors = [flavor for flavor in flavors if flavor not in self._valid_flavors]
            raise ValueError(f"Invalid flavors: {invalid_flavors}. Choose a different flavor from {self._valid_flavors}.")

    def set_size(self, size):
        size = size.lower()
        if size in self._size_costs:
            self.size = size # Assign the size 
            # Calculate the total cost with size base cost + flavor costs
            self._cost = self._size_costs[size] + 0.15 * len(self._flavors)
        else:
            raise ValueError(f"Invalid size: {size}. Choose a different size from {list(self._size_costs.keys())}.")



