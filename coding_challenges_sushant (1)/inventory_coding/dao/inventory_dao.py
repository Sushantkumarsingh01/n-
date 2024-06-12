import logging
from entities.Item import Item
from exceptions.item_not_found_exception import ItemNotFoundException

logging.basicConfig(level=logging.INFO)

class Inventory:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)
        logging.info("Item added: {}".format(item))

    def remove_item(self, item_id):
        item_to_remove = None
        for item in self._items:
            if item.id == item_id:
                item_to_remove = item
                break
        if item_to_remove:
            self._items.remove(item_to_remove)
            logging.info("Item removed: {}".format(item_to_remove))
        else:
            raise ItemNotFoundException("Item with ID {} not found.".format(item_id))

    def search_item_by_id(self, item_id):
        for item in self._items:
            if item.id == item_id:
                logging.info("Item found by ID {}: {}".format(item_id, item))
                return item
        raise ItemNotFoundException("Item with ID {} not found.".format(item_id))

    def search_item_by_name(self, name):
        for item in self._items:
            if item.name.lower() == name.lower():
                logging.info("Item found by name {}: {}".format(name, item))
                return item
        raise ItemNotFoundException("Item with name {} not found.".format(name))

    def return_sorted_items_by_price(self):
        sorted_items = sorted(self._items, key=lambda x: x.price, reverse=True)
        logging.info("Items sorted by price in descending order.")
        return sorted_items

    def return_items_of_type(self, item_type):
        items_of_type = []
        for item in self._items:
            if isinstance(item, item_type):
                items_of_type.append(item)
        logging.info("Items of type {} retrieved.".format(item_type.__name__))
        return items_of_type

    def get_inventory_details(self):
        details = [item for item in self._items]
        logging.info("Inventory details retrieved.")
        return details

    @staticmethod
    def _get_price(item):
        return item.price