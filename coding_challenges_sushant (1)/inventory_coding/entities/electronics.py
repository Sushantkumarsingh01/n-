from entities.Item import Item

class Electronics(Item):
    def __init__(self, id, name, price, quantity, warranty_period, brand):
        super().__init__(id, name, price, quantity)
        self._warranty_period = warranty_period
        self._brand = brand

    @property
    def warranty_period(self):
        return self._warranty_period

    @property
    def brand(self):
        return self._brand

    def __str__(self):
        return "Electronics(ID: {}, Name: {}, Price: ${}, Quantity: {}, Warranty Period: {} months, Brand: {})".format(
            self.id, self.name, self.price, self.quantity, self.warranty_period, self.brand
        )