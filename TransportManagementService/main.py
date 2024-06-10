import logging
import logSettings
from dao.TransportManagementServiceImpl import TransportManagementServiceImpl

from exception.VehicleNotFoundException import VehicleNotFoundException
from exception.BookingNotFoundException import BookingNotFoundException
from entity.Vehicle import Vehicle







class TransportManagementApp:
    def __init__(self):
        self.service = TransportManagementServiceImpl()
        self.current_user_role = None
        self.current_user_id = None


    def display_menu(self):
        print("Menu:")
        print("1. Add Vehicle")
        print("2. Update Vehicle")
        print("3. Delete Vehicle")
        print("4. Schedule Trip")
        print("5. Cancel Trip")
        print("6. Book Trip")
        print("7. Cancel Booking")
        print("8. Allocate Driver")
        print("9. Deallocate Driver")
        print("10. Get Bookings By Passenger")
        print("11. Get Bookings By Trip")
        print("12. Get Available Drivers")
        print("0. Exit")

    def run(self):
        while True:
            print("\nWelcome to Transport Management System! ")
            print("1. Login as Existing Customer")
            print("2. Register as New Customer")
            print("3. Login as Admin")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == "0":
                print("Exiting...")
                break
            elif choice == "1":

                self.login_customer()

            elif choice == "2":
                self.register_customer()
            elif choice == "3":
                self.login_admin()
            else:
                print("Invalid choice. Please try again.")

    def login_customer(self):
        try:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            role = self.service.authenticate_user(username, password)
            logger.info("Existing Customer Login")

            if role == "customer":
                print("Login as Customer! Welcome Customer!")
                self.customer_operations()
            else:
                print("Invalid username or password. Please try again.")
        except Exception as e:
            print(f"Error: {e}")



    def register_customer(self):
        try:
            print("\nPlease enter your details to register as a Customer:")
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            phone_number = input("Enter your phone number: ")
            email = input("Enter your email: ")
            username = input("Enter your desired username: ")
            password = input("Enter your password: ")

            if self.service.register_user(first_name, last_name, phone_number, email, username, password, "customer"):
                print("Registration successful! WELCOME ")
            else:
                print("Failed to register. Please try again.")
        except Exception as e:
            print(f"Error: {e}")



    def login_admin(self):
        try:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if self.service.authenticate_admin(username, password):
                print("Login successful! Welcome Admin!")
                logger.info("Existing Admin Login")
                self.current_user_role = "admin"
                self.admin_operations()
            else:
                print("Invalid username/password or user is not an admin.")
        except Exception as e:
            print(f"Error: {e}")



    def admin_operations(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "0":
                print("Exiting...")
                break
            elif choice == "1":
                self.add_vehicle()
            elif choice == "2":
                self.update_vehicle()
            elif choice == "3":
                self.delete_vehicle()
            elif choice == "4":
                self.schedule_trip()
            elif choice == "5":
                self.cancel_trip()
            elif choice == "6":
                self.book_trip()
            elif choice == "7":
                self.cancel_booking()
            elif choice == "8":
                self.allocate_driver()
            elif choice == "9":
                self.deallocate_driver()
            elif choice == "10":
                self.get_bookings_by_passenger()
            elif choice == "11":
                self.get_bookings_by_trip()
            elif choice == "12":
                self.get_available_drivers()
            else:
                print("Invalid choice. Please try again.")

    def customer_operations(self):
        while True:
            print("\nCustomer Menu:")
            print("1. Book Trip")
            print("2. Cancel Booking")
            print("3. Get Bookings By Passenger")
            print("4. Get Bookings By Trip")
            print("0. Logout")
            choice = input("Enter your choice: ")

            if choice == "0":
                print("Logging out...")
                self.current_user_role = None
                break
            elif choice == "1":
                self.book_trip()
            elif choice == "2":
                self.cancel_booking()
            elif choice == "3":
                self.get_bookings_by_passenger()
            elif choice == "4":
                self.get_bookings_by_trip()
            else:
                print("Invalid choice. Please try again.")

    def add_vehicle(self):
        try:
            model = input("Enter vehicle model: ")
            capacity = float(input("Enter vehicle capacity: "))
            vehicle_type = input("Enter vehicle type (e.g., Truck, Van, Bus): ")
            status = input("Enter vehicle status (e.g., Available, On Trip, Maintenance): ")
            vehicle = Vehicle(model=model, capacity=capacity, type=vehicle_type, status=status)
            if self.service.addVehicle(vehicle):
                print("Vehicle added successfully.")
            else:
                print("Failed to add vehicle.")
        except Exception as e:
            print(f"Error: {e}")

    def update_vehicle(self):
        try:
            vehicle_id = int(input("Enter vehicle ID you want to update: "))
            model = input("Enter new vehicle model: ")
            capacity = float(input("Enter new vehicle capacity: "))
            vehicle_type = input("Enter new vehicle type (e.g., Truck, Van, Bus): ")
            status = input("Enter new vehicle status (e.g., Available, On Trip, Maintenance): ")
            vehicle = Vehicle(vehicle_id=vehicle_id, model=model, capacity=capacity, type=vehicle_type, status=status)
            if self.service.updateVehicle(vehicle):
                print("Vehicle updated successfully.")
            else:
                print("Failed to update vehicle.")
        except VehicleNotFoundException:
            print("Vehicle not found.")
        except Exception as e:
            print(f"Error: {e}")

    def delete_vehicle(self):
        try:
            vehicle_id = int(input("Enter vehicle ID you want to delete: "))
            if self.service.deleteVehicle(vehicle_id):
                print("Vehicle deleted successfully.")
            else:
                print("Failed to delete vehicle.")
        except VehicleNotFoundException:
            print("Vehicle not found.")
        except Exception as e:
            print(f"Error: {e}")

    def show_available_routes(self):
        routes = self.service.get_available_routes()
        if routes:
            print("Available Routes:")
            for route in routes:
                print(f"Route ID: {route[0]}, Start: {route[1]}, Destination: {route[2]}")
        else:
            print("No routes available.")

    def schedule_trip(self):
        try:
            self.show_available_routes()  # Show available routes here

            route_id = int(input("Enter route ID: "))
            vehicle_id = int(input("Enter vehicle ID: "))
            departure_date = input("Enter departure date (YYYY-MM-DD): ")
            arrival_date = input("Enter arrival date (YYYY-MM-DD): ")
            trip_type = input("Enter trip type (e.g., Freight, Passenger): ")
            max_passengers = int(input("Enter maximum number of passengers: "))
            if self.service.scheduleTrip(vehicle_id, route_id, departure_date, arrival_date, trip_type, max_passengers):
                print("Trip scheduled successfully! Happy & Safe Journey! ")
            else:
                print("Failed to schedule trip. Please try again.")
        except ValueError:
            print("Invalid input. Please enter valid data.")

    def cancel_trip(self):
        try:
            trip_id = int(input("Enter trip ID to cancel: "))
            if self.service.cancelTrip(trip_id):
                print("Trip canceled successfully! see you soon ")
            else:
                print("Failed to cancel trip.")
        except Exception as e:
            print(f"Error: {e}")

    def book_trip(self):
        try:
            trip_id = int(input("Enter trip ID: "))
            passenger_id = int(input("Enter passenger ID: "))
            booking_date = input("Enter booking date (YYYY-MM-DD): ")
            if self.service.bookTrip(trip_id, passenger_id, booking_date):
                print("Trip booked successfully. Happy Journey!")
            else:
                print("Failed to book trip.")
        except Exception as e:
            print(f"Error: {e}")

    def cancel_booking(self):
        try:
            booking_id = int(input("Enter booking ID to cancel: "))
            if self.service.cancelBooking(booking_id):
                print("Booking canceled successfully.")
            else:
                print("Failed to cancel booking.")
        except BookingNotFoundException:
            print("Booking not found.")
        except Exception as e:
            print(f"Error: {e}")

    def allocate_driver(self):
        try:
            trip_id = int(input("Enter trip ID: "))
            driver_id = int(input("Enter driver ID to allocate: "))
            if self.service.allocateDriver(trip_id, driver_id):
                print("Driver allocated successfully.")
            else:
                print("Failed to allocate driver.")
        except Exception as e:
            print(f"Error: {e}")

    def deallocate_driver(self):
        try:
            trip_id = int(input("Enter trip ID to deallocate: "))
            if self.service.deallocateDriver(trip_id):
                print("Driver deallocated successfully.")
            else:
                print("Failed to deallocate driver.")
        except Exception as e:
            print(f"Error: {e}")

    def get_bookings_by_passenger(self):
        try:
            passenger_id = int(input("Enter passenger ID: "))
            bookings = self.service.getBookingsByPassenger(passenger_id)
            for booking in bookings:
                print(booking)
        except Exception as e:
            print(f"Error: {e}")

    def get_bookings_by_trip(self):
        try:
            trip_id = int(input("Enter trip ID: "))
            bookings = self.service.getBookingsByTrip(trip_id)
            for booking in bookings:
                print(booking)
        except Exception as e:
            print(f"Error: {e}")

    def get_available_drivers(self):
        try:
            drivers = self.service.getAvailableDrivers()
            for driver in drivers:
                print(driver)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":


   # logging.info("Information message")
    logger = logging.getLogger("my_log")
    logger.warning("Warning message")
    logger.error("Error message")
    app = TransportManagementApp()
    app.run()











































































"""
from dao.TransportManagementServiceImpl import TransportManagementServiceImpl
from exception.VehicleNotFoundException import VehicleNotFoundException
from exception.BookingNotFoundException import BookingNotFoundException
from entity.Vehicle import Vehicle
from colorama import Fore, Back, Style, init
import logSettings
import logging.config


class TransportManagementApp:
    def __init__(self):
        self.service = TransportManagementServiceImpl()
        self.current_user_role = None
        self.current_user_id = None
        init(autoreset=True)  # Initialize colorama

    def display_menu(self):
        print(Fore.BLUE + Style.BRIGHT + "╔══════════════════════════════════════════════════════════════════════════╗")
        print(Fore.BLUE + Style.BRIGHT + "║ " + Fore.YELLOW + Style.BRIGHT + "Main Menu" + Fore.BLUE + "                                                                ║")
        print(Fore.BLUE + Style.BRIGHT + "╠══════════════════════════════════════════════════════════════════════════╣")
        print(Fore.CYAN + "║ 1. Add Vehicle                                                           ║")
        print(Fore.CYAN + "║ 2. Update Vehicle                                                        ║")
        print(Fore.CYAN + "║ 3. Delete Vehicle                                                        ║")
        print(Fore.CYAN + "║ 4. Schedule Trip                                                         ║")
        print(Fore.CYAN + "║ 5. Cancel Trip                                                           ║")
        print(Fore.CYAN + "║ 6. Book Trip                                                             ║")
        print(Fore.CYAN + "║ 7. Cancel Booking                                                        ║")
        print(Fore.CYAN + "║ 8. Allocate Driver                                                       ║")
        print(Fore.CYAN + "║ 9. Deallocate Driver                                                     ║")
        print(Fore.CYAN + "║ 10. Get Bookings By Passenger                                            ║")
        print(Fore.CYAN + "║ 11. Get Bookings By Trip                                                 ║")
        print(Fore.CYAN + "║ 12. Get Available Drivers                                                ║")
        print(Fore.CYAN + "║ 0. Exit                                                                  ║")
        print(Fore.BLUE + Style.BRIGHT + "╚══════════════════════════════════════════════════════════════════════════╝")

    def run(self):
        while True:
            print(Fore.GREEN + Style.BRIGHT + "\n╔═══════════════════════════════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "║   " + Fore.YELLOW + Style.BRIGHT + "Welcome to Transport Management System!" + Fore.GREEN + "             ║")
            print(Fore.GREEN + Style.BRIGHT + "╠═══════════════════════════════════════════════════════╣")
            print(Fore.MAGENTA + "║ 1. Login as Existing Customer                         ║")
            print(Fore.MAGENTA + "║ 2. Register as New Customer                           ║")
            print(Fore.MAGENTA + "║ 3. Login as Admin                                     ║")
            print(Fore.MAGENTA + "║ 0. Exit                                               ║")
            print(Fore.GREEN + Style.BRIGHT + "╚═══════════════════════════════════════════════════════╝")
            choice = input(Fore.YELLOW + "Enter your choice: ")

            if choice == "0":
                print(Fore.RED + "Exiting...")
                break
            elif choice == "1":
                self.login_customer()
            elif choice == "2":
                self.register_customer()
            elif choice == "3":
                self.login_admin()
            else:
                print(Fore.RED + "Invalid choice. Please try again.")

    def login_customer(self):
        try:
            print(Fore.GREEN + Style.BRIGHT + "\n╔══════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "║     Customer Login           ║")
            print(Fore.GREEN + Style.BRIGHT + "╚══════════════════════════════╝")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            role = self.service.authenticate_user(username, password)
            if role == "admin":
                print("Login as Admin")
                # Handle admin operations
            elif role == "customer":
                print("Login as Customer! Welcome Customer!")
                self.customer_operations()
            else:
                print(Fore.RED + "Invalid username or password. Please try again.")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def register_customer(self):
        try:
            print(Fore.GREEN + Style.BRIGHT + "\n╔════════════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "║     Register as New Customer       ║")
            print(Fore.GREEN + Style.BRIGHT + "╚════════════════════════════════════╝")
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            phone_number = input("Enter your phone number: ")
            email = input("Enter your email: ")
            username = input("Enter your desired username: ")
            password = input("Enter your password: ")

            if self.service.register_user(first_name, last_name, phone_number, email, username, password, "customer"):
                print(Fore.GREEN + "Registration successful! WELCOME ")
            else:
                print(Fore.RED + "Failed to register. Please try again.")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def login_admin(self):
        try:
            print(Fore.GREEN + Style.BRIGHT + "\n╔══════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "║       Admin Login            ║")
            print(Fore.GREEN + Style.BRIGHT + "╚══════════════════════════════╝")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if self.service.authenticate_admin(username, password):
                print(Fore.GREEN + "Login successful! Welcome Admin!")
                self.current_user_role = "admin"
                self.admin_operations()
            else:
                print(Fore.RED + "Invalid username/password or user is not an admin.")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def admin_operations(self):
        while True:
            self.display_menu()
            choice = input(Fore.YELLOW + "Enter your choice: ")

            if choice == "0":
                print(Fore.RED + "Exiting...")
                break
            elif choice == "1":
                self.add_vehicle()
            elif choice == "2":
                self.update_vehicle()
            elif choice == "3":
                self.delete_vehicle()
            elif choice == "4":
                self.schedule_trip()
            elif choice == "5":
                self.cancel_trip()
            elif choice == "6":
                self.book_trip()
            elif choice == "7":
                self.cancel_booking()
            elif choice == "8":
                self.allocate_driver()
            elif choice == "9":
                self.deallocate_driver()
            elif choice == "10":
                self.get_bookings_by_passenger()
            elif choice == "11":
                self.get_bookings_by_trip()
            elif choice == "12":
                self.get_available_drivers()
            else:
                print(Fore.RED + "Invalid choice. Please try again.")

    def customer_operations(self):
        while True:
            print(Fore.GREEN + Style.BRIGHT + "\n╔══════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "║       Customer Menu          ║")
            print(Fore.GREEN + Style.BRIGHT + "╚══════════════════════════════╝")
            print(Fore.CYAN + "1. Book Trip")
            print(Fore.CYAN + "2. Cancel Booking")
            print(Fore.CYAN + "3. Get Bookings By Passenger")
            print(Fore.CYAN + "4. Get Bookings By Trip")
            print(Fore.CYAN + "0. Logout")
            choice = input(Fore.YELLOW + "Enter your choice: ")

            if choice == "0":
                print(Fore.RED + "Logging out...")
                self.current_user_role = None
                break
            elif choice == "1":
                self.book_trip()
            elif choice == "2":
                self.cancel_booking()
            elif choice == "3":
                self.get_bookings_by_passenger()
            elif choice == "4":
                self.get_bookings_by_trip()
            else:
                print(Fore.RED + "Invalid choice. Please try again.")

    def add_vehicle(self):
        try:
            print(Fore.GREEN + Style.BRIGHT + "\n╔══════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "║        Add Vehicle           ║")
            print(Fore.GREEN + Style.BRIGHT + "╚══════════════════════════════╝")
            model = input("Enter vehicle model: ")
            capacity = float(input("Enter vehicle capacity: "))
            vehicle_type = input("Enter vehicle type (e.g., Truck, Van, Bus): ")
            status = input("Enter vehicle status (e.g., Available, On Trip, Maintenance): ")
            vehicle = Vehicle(model=model, capacity=capacity, type=vehicle_type, status=status)
            if self.service.addVehicle(vehicle):
                print(Fore.GREEN + "Vehicle added successfully.")
            else:
                print(Fore.RED + "Failed to add vehicle.")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def update_vehicle(self):
        try:
            print(Fore.GREEN + Style.BRIGHT + "\n╔══════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "║      Update Vehicle          ║")
            print(Fore.GREEN + Style.BRIGHT + "╚══════════════════════════════╝")
            vehicle_id = int(input("Enter vehicle ID you want to update: "))
            model = input("Enter new vehicle model: ")
            capacity = float(input("Enter new vehicle capacity: "))
            vehicle_type = input("Enter new vehicle type (e.g., Truck, Van, Bus): ")
            status = input("Enter new vehicle status (e.g., Available, On Trip, Maintenance): ")
            vehicle = Vehicle(vehicle_id=vehicle_id, model=model, capacity=capacity, type=vehicle_type, status=status)
            if self.service.updateVehicle(vehicle):
                print(Fore.GREEN + "Vehicle updated successfully.")
            else:
                print(Fore.RED + "Failed to update vehicle.")
        except VehicleNotFoundException:
            print(Fore.RED + "Vehicle not found.")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def delete_vehicle(self):
        try:
            print(Fore.GREEN + Style.BRIGHT + "\n╔══════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "║      Delete Vehicle          ║")
            print(Fore.GREEN + Style.BRIGHT + "╚══════════════════════════════╝")
            vehicle_id = int(input("Enter vehicle ID you want to delete: "))
            if self.service.deleteVehicle(vehicle_id):
                print(Fore.GREEN + "Vehicle deleted successfully.")
            else:
                print(Fore.RED + "Failed to delete vehicle.")
        except VehicleNotFoundException:
            print(Fore.RED + "Vehicle not found.")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def show_available_routes(self):
        routes = self.service.get_available_routes()
        if routes:
            print(Fore.GREEN + Style.BRIGHT + "╔═════════════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "║         Available Routes            ║")
            print(Fore.GREEN + Style.BRIGHT + "╚═════════════════════════════════════╝")
            for route in routes:
                print(Fore.CYAN + f"Route ID: {route[0]}, Start: {route[1]}, Destination: {route[2]}")
        else:
            print(Fore.RED + "No routes available.")

    def schedule_trip(self):
        try:
            self.show_available_routes()  # Show available routes here

            route_id = int(input("Enter route ID: "))
            vehicle_id = int(input("Enter vehicle ID: "))
            departure_date = input("Enter departure date (YYYY-MM-DD): ")
            arrival_date = input("Enter arrival date (YYYY-MM-DD): ")
            trip_type = input("Enter trip type (e.g., Freight, Passenger): ")
            max_passengers = int(input("Enter maximum number of passengers: "))
            if self.service.scheduleTrip(vehicle_id, route_id, departure_date, arrival_date, trip_type, max_passengers):
                print(Fore.GREEN + "Trip scheduled successfully! Happy & Safe Journey! ")
            else:
                print(Fore.RED + "Failed to schedule trip. Please try again.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter valid data.")

    def cancel_trip(self):
        try:
            print(Fore.GREEN + Style.BRIGHT + "\n╔══════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "║       Cancel Trip            ║")
            print(Fore.GREEN + Style.BRIGHT + "╚══════════════════════════════╝")
            trip_id = int(input("Enter trip ID to cancel: "))
            if self.service.cancelTrip(trip_id):
                print(Fore.GREEN + "Trip canceled successfully! see you soon ")
            else:
                print(Fore.RED + "Failed to cancel trip.")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def book_trip(self):
        try:
            print(Fore.GREEN + Style.BRIGHT + "\n╔══════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "║        Book Trip             ║")
            print(Fore.GREEN + Style.BRIGHT + "╚══════════════════════════════╝")
            trip_id = int(input("Enter trip ID: "))
            passenger_id = int(input("Enter passenger ID: "))
            booking_date = input("Enter booking date (YYYY-MM-DD): ")
            if self.service.bookTrip(trip_id, passenger_id, booking_date):
                print(Fore.GREEN + "Trip booked successfully. Happy Journey!")
            else:
                print(Fore.RED + "Failed to book trip.")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def cancel_booking(self):
        try:
            print(Fore.GREEN + Style.BRIGHT + "\n╔══════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "║       Cancel Booking         ║")
            print(Fore.GREEN + Style.BRIGHT + "╚══════════════════════════════╝")
            booking_id = int(input("Enter booking ID to cancel: "))
            if self.service.cancelBooking(booking_id):
                print(Fore.GREEN + "Booking canceled successfully.")
            else:
                print(Fore.RED + "Failed to cancel booking.")
        except BookingNotFoundException:
            print(Fore.RED + "Booking not found.")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def allocate_driver(self):
        try:
            print(Fore.GREEN + Style.BRIGHT + "\n╔══════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "║      Allocate Driver         ║")
            print(Fore.GREEN + Style.BRIGHT + "╚══════════════════════════════╝")
            trip_id = int(input("Enter trip ID: "))
            driver_id = int(input("Enter driver ID to allocate: "))
            if self.service.allocateDriver(trip_id, driver_id):
                print(Fore.GREEN + "Driver allocated successfully.")
            else:
                print(Fore.RED + "Failed to allocate driver.")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def deallocate_driver(self):
        try:
            print(Fore.GREEN + Style.BRIGHT + "\n╔══════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "║     Deallocate Driver        ║")
            print(Fore.GREEN + Style.BRIGHT + "╚══════════════════════════════╝")
            trip_id = int(input("Enter trip ID to deallocate: "))
            if self.service.deallocateDriver(trip_id):
                print(Fore.GREEN + "Driver deallocated successfully.")
            else:
                print(Fore.RED + "Failed to deallocate driver.")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def get_bookings_by_passenger(self):
        try:
            print(Fore.GREEN + Style.BRIGHT + "\n╔══════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "║  Get Bookings By Passenger   ║")
            print(Fore.GREEN + Style.BRIGHT + "╚══════════════════════════════╝")
            passenger_id = int(input("Enter passenger ID: "))
            bookings = self.service.getBookingsByPassenger(passenger_id)
            for booking in bookings:
                print(Fore.CYAN + str(booking))
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def get_bookings_by_trip(self):
        try:
            print(Fore.GREEN + Style.BRIGHT + "\n╔══════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "║    Get Bookings By Trip      ║")
            print(Fore.GREEN + Style.BRIGHT + "╚══════════════════════════════╝")
            trip_id = int(input("Enter trip ID: "))
            bookings = self.service.getBookingsByTrip(trip_id)
            for booking in bookings:
                print(Fore.CYAN + str(booking))
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def get_available_drivers(self):
        try:
            print(Fore.GREEN + Style.BRIGHT + "\n╔══════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "║     Available Drivers        ║")
            print(Fore.GREEN + Style.BRIGHT + "╚══════════════════════════════╝")
            drivers = self.service.getAvailableDrivers()
            for driver in drivers:
                print(Fore.CYAN + str(driver))
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

if __name__ == "__main__":
    logging.config.dictConfig(logSettings.LOG_SETTINGS)

    logging.info("Information message")
    logger = logging.getLogger("my_log")
    logging.warning("Warning message")
    logging.error("Error message")
    app = TransportManagementApp()
    app.run()


"""





































