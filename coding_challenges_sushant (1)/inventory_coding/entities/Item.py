

from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, id, name, price, quantity):
        self._id = id
        self._name = name
        self._price = price
        self._quantity = quantity

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

    @abstractmethod
    def __str__(self):
        pass







