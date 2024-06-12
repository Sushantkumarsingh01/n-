from entities.Item import Item

class Clothing(Item):
    def __init__(self, id: int, name: str, price: float, quantity: int, size: str, color: str):
        super().__init__(id, name, price, quantity)
        self._color = None
        self.size = None


    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size

    @property
    def color(self):
        return self._color

    @size.setter
    def size(self, value):
        self._size = value

    @color.setter
    def color(self, value):
        self._color = value






















