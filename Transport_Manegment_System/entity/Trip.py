class Trip:
    def __init__(self, trip_id=None, vehicle_id=None, route_id=None, departure_date=None, arrival_date=None, status=None, driver_id=None):
        self._trip_id = trip_id
        self._vehicle_id = vehicle_id
        self._route_id = route_id
        self._departure_date = departure_date
        self._arrival_date = arrival_date
        self._status = status
        self._driver_id = driver_id

    # Getters
    def get_trip_id(self):
        return self._trip_id

    def get_vehicle_id(self):
        return self._vehicle_id

    def get_route_id(self):
        return self._route_id

    def get_departure_date(self):
        return self._departure_date

    def get_arrival_date(self):
        return self._arrival_date

    def get_status(self):
        return self._status

    def get_driver_id(self):
        return self._driver_id

    # Setters
    def set_trip_id(self, trip_id):
        self._trip_id = trip_id

    def set_vehicle_id(self, vehicle_id):
        self._vehicle_id = vehicle_id

    def set_route_id(self, route_id):
        self._route_id = route_id

    def set_departure_date(self, departure_date):
        self._departure_date = departure_date

    def set_arrival_date(self, arrival_date):
        self._arrival_date = arrival_date

    def set_status(self, status):
        self._status = status

    def set_driver_id(self, driver_id):
        self._driver_id = driver_id

    def __str__(self):
        return f"Trip(ID: {self._trip_id}, VehicleID: {self._vehicle_id}, RouteID: {self._route_id}, DepartureDate: {self._departure_date}, ArrivalDate: {self._arrival_date}, Status: {self._status}, DriverID: {self._driver_id})"






















"""class Trip:
    def __init__(self, trip_id=None, vehicle_id=None, route_id=None, departure_date=None, arrival_date=None, status=None, trip_type='Freight', max_passengers=None):
        self._trip_id = trip_id
        self._vehicle_id = vehicle_id
        self._route_id = route_id
        self._departure_date = departure_date
        self._arrival_date = arrival_date
        self._status = status
        self._trip_type = trip_type
        self._max_passengers = max_passengers

    def get_trip_id(self):
        return self._trip_id

    def set_trip_id(self, trip_id):
        self._trip_id = trip_id

    def get_vehicle_id(self):
        return self._vehicle_id

    def set_vehicle_id(self, vehicle_id):
        self._vehicle_id = vehicle_id

    def get_route_id(self):
        return self._route_id

    def set_route_id(self, route_id):
        self._route_id = route_id

    def get_departure_date(self):
        return self._departure_date

    def set_departure_date(self, departure_date):
        self._departure_date = departure_date

    def get_arrival_date(self):
        return self._arrival_date

    def set_arrival_date(self, arrival_date):
        self._arrival_date = arrival_date

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_trip_type(self):
        return self._trip_type

    def set_trip_type(self, trip_type):
        self._trip_type = trip_type

    def get_max_passengers(self):
        return self._max_passengers

    def set_max_passengers(self, max_passengers):
        self._max_passengers = max_passengers
 """