import logging
from service.inventory_service_provider import InventoryServiceProviderImpl
from entities.electronics import Electronics
from entities.clothing import Clothing
from entities.grocery import Grocery
from exceptions.item_not_found_exception import ItemNotFoundException

logging.basicConfig(level=logging.INFO)

def display_menu():
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Search Item by ID")
    print("4. Search Item by Name")
    print("5. List Items Sorted by Price")
    print("6. List Items of Specific Type")
    print("7. Exit")

def add_item(inventory_service):
    item_type = input("Enter item type (Electronics/Clothing/Grocery): ").strip().lower()
    id = int(input("Enter item ID: "))
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))

    if item_type == "electronics":
        warranty_period = int(input("Enter warranty period (months): "))
        brand = input("Enter brand: ")
        item = Electronics(id=id, name=name, price=price, quantity=quantity, warranty_period=warranty_period, brand=brand)
    elif item_type == "clothing":
        size = input("Enter size: ")
        color = input("Enter color: ")
        item = Clothing(id=id, name=name, price=price, quantity=quantity, size=size, color=color)
    elif item_type == "grocery":
        expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
        brand = input("Enter brand: ")
        item = Grocery(id=id, name=name, price=price, quantity=quantity, expiry_date=expiry_date, brand=brand)
    else:
        print("Invalid item type.")
        return

    inventory_service.add_item(item)
    print("Item added successfully.")

def remove_item(inventory_service):
    item_id = int(input("Enter item ID to remove: "))
    try:
        inventory_service.remove_item(item_id)
        print("Item removed successfully.")
    except ItemNotFoundException as e:
        print(e.message)

def search_item_by_id(inventory_service):
    item_id = int(input("Enter item ID to search: "))
    try:
        item = inventory_service.search_item_by_id(item_id)
        print(item)
    except ItemNotFoundException as e:
        print(e.message)

def search_item_by_name(inventory_service):
    name = input("Enter item name to search: ")
    try:
        item = inventory_service.search_item_by_name(name)
        print(item)
    except ItemNotFoundException as e:
        print(e.message)

def list_items_sorted_by_price(inventory_service):
    sorted_items = inventory_service.return_sorted_items_by_price()
    for item in sorted_items:
        print(item)

def list_items_of_type(inventory_service):
    item_type = input("Enter item type (Electronics/Clothing/Grocery): ").strip().lower()
    if item_type == "electronics":
        items = inventory_service.return_items_of_type(Electronics)
    elif item_type == "clothing":
        items = inventory_service.return_items_of_type(Clothing)
    elif item_type == "grocery":
        items = inventory_service.return_items_of_type(Grocery)
    else:
        print("Invalid item type.")
        return

    for item in items:
        print(item)

def main():
    inventory_service = InventoryServiceProviderImpl()
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: ").strip())
            if choice == 1:
                add_item(inventory_service)
            elif choice == 2:
                remove_item(inventory_service)
            elif choice == 3:
                search_item_by_id(inventory_service)
            elif choice == 4:
                search_item_by_name(inventory_service)
            elif choice == 5:
                list_items_sorted_by_price(inventory_service)
            elif choice == 6:
                list_items_of_type(inventory_service)
            elif choice == 7:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except ItemNotFoundException as e:
            print(e.message)
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            break

if __name__ == "__main__":
    main()
