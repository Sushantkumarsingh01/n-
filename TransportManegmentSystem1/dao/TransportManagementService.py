from abc import ABC, abstractmethod

class TransportManagementService(ABC):
    @abstractmethod
    def addVehicle(self, vehicle):
        pass

    @abstractmethod
    def updateVehicle(self, vehicle):
        pass

    @abstractmethod
    def deleteVehicle(self, vehicle_id):
        pass

    @abstractmethod
    def scheduleTrip(self, vehicle_id, route_id, departure_date, arrival_date):
        pass

    @abstractmethod
    def cancelTrip(self, trip_id):
        pass

    @abstractmethod
    def bookTrip(self, trip_id, passenger_id, booking_date):
        pass

    @abstractmethod
    def cancelBooking(self, booking_id):
        pass

    @abstractmethod
    def allocateDriver(self, trip_id, driver_id):
        pass

    @abstractmethod
    def deallocateDriver(self, trip_id):
        pass

    @abstractmethod
    def getBookingsByPassenger(self, passenger_id):
        pass

    @abstractmethod
    def getBookingsByTrip(self, trip_id):
        pass

    @abstractmethod
    def getAvailableDrivers(self):
        pass



























"""from abc import ABC, abstractmethod

class TransportManagementService(ABC):
    @abstractmethod
    def addVehicle(self, vehicle):
        pass

    @abstractmethod
    def updateVehicle(self, vehicle):
        pass

    @abstractmethod
    def deleteVehicle(self, vehicle_id):
        pass

    @abstractmethod
    def scheduleTrip(self, vehicle_id, route_id, departure_date, arrival_date):
        pass

    @abstractmethod
    def cancelTrip(self, trip_id):
        pass

    @abstractmethod
    def bookTrip(self, trip_id, passenger_id, booking_date):
        pass

    @abstractmethod
    def cancelBooking(self, booking_id):
        pass

    @abstractmethod
    def allocateDriver(self, trip_id, driver_id):
        pass

    @abstractmethod
    def deallocateDriver(self, trip_id):
        pass

    @abstractmethod
    def getBookingsByPassenger(self, passenger_id):
        pass

    @abstractmethod
    def getBookingsByTrip(self, trip_id):
        pass

    @abstractmethod
    def getAvailableDrivers(self):
        pass"""
