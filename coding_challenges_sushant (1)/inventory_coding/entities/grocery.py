
from entities.Item import Item

class Grocery(Item):
    def __init__(self, id: int, name: str, price: float, quantity: int, expiry_date: str, brand: str):
        super().__init__(id, name, price, quantity)
        self._expiry_date = None
        self.brand = None

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity


    @property
    def expiry_date(self):
        return self._expiry_date

    @property
    def brand(self):
        return self._brand

