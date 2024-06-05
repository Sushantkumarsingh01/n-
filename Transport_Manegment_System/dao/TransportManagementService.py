from abc import ABC, abstractmethod
from entity import Vehicle, Booking
from typing import List

class TransportManagementService(ABC):

    @abstractmethod
    def addVehicle(self, vehicle: Vehicle) -> bool:
        pass

    @abstractmethod
    def updateVehicle(self, vehicle: Vehicle) -> bool:
        pass

    @abstractmethod
    def deleteVehicle(self, vehicleId: int) -> bool:
        pass

    @abstractmethod
    def scheduleTrip(self, vehicleId: int, routeId: int, departureDate: str, arrivalDate: str) -> bool:
        pass

    @abstractmethod
    def cancelTrip(self, tripId: int) -> bool:
        pass

    @abstractmethod
    def bookTrip(self, tripId: int, passengerId: int, bookingDate: str) -> bool:
        pass

    @abstractmethod
    def cancelBooking(self, bookingId: int) -> bool:
        pass

    @abstractmethod
    def allocateDriver(self, tripId: int, driverId: int) -> bool:
        pass

    @abstractmethod
    def deallocateDriver(self, tripId: int) -> bool:
        pass

    @abstractmethod
    def getBookingsByPassenger(self, passengerId: int) -> List[Booking]:
        pass

    @abstractmethod
    def getBookingsByTrip(self, tripId: int) -> List[Booking]:
        pass

    @abstractmethod
    def getAvailableDrivers(self) -> List[int]:
        pass






















"""from abc import ABC, abstractmethod
from entity import Vehicle, Booking, Driver

class TransportManagementService(ABC):

    @abstractmethod
    def addVehicle(self, vehicle: Vehicle) -> bool:
        pass

    @abstractmethod
    def updateVehicle(self, vehicle: Vehicle) -> bool:
        pass

    @abstractmethod
    def deleteVehicle(self, vehicleId: int) -> bool:
        pass

    @abstractmethod
    def scheduleTrip(self, vehicleId: int, routeId: int, departureDate: str, arrivalDate: str) -> bool:
        pass

    @abstractmethod
    def cancelTrip(self, tripId: int) -> bool:
        pass

    @abstractmethod
    def bookTrip(self, tripId: int, passengerId: int, bookingDate: str) -> bool:
        pass

    @abstractmethod
    def cancelBooking(self, bookingId: int) -> bool:
        pass

    @abstractmethod
    def allocateDriver(self, tripId: int, driverId: int) -> bool:
        pass

    @abstractmethod
    def deallocateDriver(self, tripId: int) -> bool:
        pass

    @abstractmethod
    def getBookingsByPassenger(self, passengerId: int) -> list:
        pass

    @abstractmethod
    def getBookingsByTrip(self, tripId: int) -> list:
        pass

    @abstractmethod
    def getAvailableDrivers(self) -> list:
        pass """
