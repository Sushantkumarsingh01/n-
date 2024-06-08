
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
            print("\nWelcome to Transport Management System!")
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
            if role == "admin":
                print("Login as Admin")
                # Handle admin operations
            elif role == "customer":
                print("Login as Customer")
                self.customer_operations()
            else:
                print("Invalid username or password. Please try again.")
        except Exception as e:
            print(f"Error: {e}")



    def register_customer(self):
        try:
            print("\nPlease enter your details to register:")
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            phone_number = input("Enter your phone number: ")
            email = input("Enter your email: ")
            username = input("Enter your desired username: ")
            password = input("Enter your password: ")

            if self.service.register_user(first_name, last_name, phone_number, email, username, password, "customer"):
                print("Registration successful!")
            else:
                print("Failed to register. Please try again.")
        except Exception as e:
            print(f"Error: {e}")



    def login_admin(self):
        try:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if self.service.authenticate_admin(username, password):
                print("Login successful!")
                self.current_user_role = "admin"
                self.admin_operations()
            else:
                print("Invalid username/password or user is not an admin.")
        except Exception as e:
            print(f"Error: {e}")

    """def register_admin(self):
        print("Please enter your details to register as admin:")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        phone_number = input("Enter your phone number: ")
        email = input("Enter your email: ")
        username = input("Enter your desired username: ")
        password = input("Enter your password: ")
        if self.service.register_user(first_name, last_name, phone_number, email, username, password, "admin"):
            print("Admin registration successful.")
        else:
            print("Failed to register admin. Please try again.")"""

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
            vehicle_id = int(input("Enter vehicle ID: "))
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
            vehicle_id = int(input("Enter vehicle ID to delete: "))
            if self.service.deleteVehicle(vehicle_id):
                print("Vehicle deleted successfully.")
            else:
                print("Failed to delete vehicle.")
        except VehicleNotFoundException:
            print("Vehicle not found.")
        except Exception as e:
            print(f"Error: {e}")

    def schedule_trip(self):
        try:
            vehicle_id = int(input("Enter vehicle ID: "))
            route_id = int(input("Enter route ID: "))
            departure_date = input("Enter departure date (YYYY-MM-DD HH:MM:SS): ")
            arrival_date = input("Enter arrival date (YYYY-MM-DD HH:MM:SS): ")
            trip_type = input("Enter trip type: ")
            max_passengers = int(input("Enter number of passengers: "))
            if self.service.scheduleTrip(vehicle_id, route_id, departure_date, arrival_date, trip_type, max_passengers):
                print("Trip scheduled successfully.")
            else:
                print("Failed to schedule trip.")
        except Exception as e:
            print(f"Error: {e}")

    def cancel_trip(self):
        try:
            trip_id = int(input("Enter trip ID to cancel: "))
            if self.service.cancelTrip(trip_id):
                print("Trip canceled successfully.")
            else:
                print("Failed to cancel trip.")
        except Exception as e:
            print(f"Error: {e}")

    def book_trip(self):
        try:
            trip_id = int(input("Enter trip ID: "))
            passenger_id = int(input("Enter passenger ID: "))
            booking_date = input("Enter booking date (YYYY-MM-DD HH:MM:SS): ")
            if self.service.bookTrip(trip_id, passenger_id, booking_date):
                print("Trip booked successfully.")
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
            driver_id = int(input("Enter driver ID: "))
            if self.service.allocateDriver(trip_id, driver_id):
                print("Driver allocated successfully.")
            else:
                print("Failed to allocate driver.")
        except Exception as e:
            print(f"Error: {e}")

    def deallocate_driver(self):
        try:
            trip_id = int(input("Enter trip ID: "))
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
    app = TransportManagementApp()
    app.run()



























"""" without admin authentication


from datetime import datetime
from dao.TransportManagementServiceImpl import TransportManagementServiceImpl
from exception.VehicleNotFoundException import VehicleNotFoundException
from exception.BookingNotFoundException import BookingNotFoundException
from entity.Vehicle import Vehicle

class TransportManagementApp:
    def __init__(self):
        self.service = TransportManagementServiceImpl()

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
            vehicle_id = int(input("Enter vehicle ID: "))
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
            vehicle_id = int(input("Enter vehicle ID to delete: "))
            if self.service.deleteVehicle(vehicle_id):
                print("Vehicle deleted successfully.")
            else:
                print("Failed to delete vehicle.")
        except VehicleNotFoundException:
            print("Vehicle not found.")
        except Exception as e:
            print(f"Error: {e}")

    def schedule_trip(self):
        try:
            vehicle_id = int(input("Enter vehicle ID: "))
            route_id = int(input("Enter route ID: "))
            departure_date = input("Enter departure date (YYYY-MM-DD HH:MM:SS): ")
            arrival_date = input("Enter arrival date (YYYY-MM-DD HH:MM:SS): ")
            trip_type = input("Enter trip type: ")
            max_passengers = int(input("Enter number of passengers: "))
            if self.service.scheduleTrip(vehicle_id, route_id, departure_date, arrival_date, trip_type, max_passengers):
                print("Trip scheduled successfully.")
            else:
                print("Failed to schedule trip.")
        except Exception as e:
            print(f"Error: {e}")

    def cancel_trip(self):
        try:
            trip_id = int(input("Enter trip ID to cancel: "))
            if self.service.cancelTrip(trip_id):
                print("Trip canceled successfully.")
            else:
                print("Failed to cancel trip.")
        except Exception as e:
            print(f"Error: {e}")

    def book_trip(self):
        try:
            trip_id = int(input("Enter trip ID: "))
            passenger_id = int(input("Enter passenger ID: "))
            booking_date = input("Enter booking date (YYYY-MM-DD HH:MM:SS): ")
            if self.service.bookTrip(trip_id, passenger_id, booking_date):
                print("Trip booked successfully.")
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
            driver_id = int(input("Enter driver ID: "))
            if self.service.allocateDriver(trip_id, driver_id):
                print("Driver allocated successfully.")
            else:
                print("Failed to allocate driver.")
        except Exception as e:
            print(f"Error: {e}")

    def deallocate_driver(self):
        try:
            trip_id = int(input("Enter trip ID: "))
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
    app = TransportManagementApp()
    app.run()


"""