
import logging
from abc import ABC, abstractmethod
from dao.inventory_dao import Inventory
from entities.Item import Item
from exceptions.item_not_found_exception import ItemNotFoundException

class IInventoryServiceProvider(ABC):
    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def remove_item(self, item_id):
        pass

    @abstractmethod
    def search_item_by_id(self, item_id):
        pass

    @abstractmethod
    def search_item_by_name(self, name):
        pass

    @abstractmethod
    def return_sorted_items_by_price(self):
        pass

    @abstractmethod
    def return_items_of_type(self, item_type):
        pass

class InventoryServiceProviderImpl(IInventoryServiceProvider):
    def __init__(self):
        self._inventory = Inventory()
    def add_item(self, item):
        self._inventory.add_item(item)
    def remove_item(self, item_id):
        self._inventory.remove_item(item_id)
    def search_item_by_id(self, item_id):
        return self._inventory.search_item_by_id(item_id)
    def search_item_by_name(self, name):
        return self._inventory.search_item_by_name(name)
    def return_sorted_items_by_price(self):
        return self._inventory.return_sorted_items_by_price()
    def return_items_of_type(self, item_type):
        return self._inventory.return_items_of_type(item_type)



