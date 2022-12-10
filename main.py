class Technic:

    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability
        self.category = None
        if self.price:
            self.category = "Бюджетный"
        else:
            self.category = "Дорогой"


    def __setattr__(self, key, value):
        if key not in ("name", "price", "availability", "category"):
            return False
        object.__setattr__(self, key, value)


    def __eq__(self, other):
        return len(self.name) == len(other.name)






