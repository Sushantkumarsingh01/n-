class Booking:
    def __init__(self, booking_id=None, trip_id=None, passenger_id=None, booking_date=None, status=None, trip_type=None, max_passengers=None):
        self._booking_id = booking_id
        self._trip_id = trip_id
        self._passenger_id = passenger_id
        self._booking_date = booking_date
        self._status = status
        self._trip_type = trip_type
        self._max_passengers = max_passengers


    def get_booking_id(self):
        return self._booking_id

    def get_trip_id(self):
        return self._trip_id

    def get_passenger_id(self):
        return self._passenger_id

    def get_booking_date(self):
        return self._booking_date

    def get_status(self):
        return self._status

    def set_booking_id(self, booking_id):
        self._booking_id = booking_id

    def set_trip_id(self, trip_id):
        self._trip_id = trip_id

    def set_passenger_id(self, passenger_id):
        self._passenger_id = passenger_id

    def set_booking_date(self, booking_date):
        self._booking_date = booking_date

    def set_status(self, status):
        self._status = status

    def __str__(self):
        return f"Booking(ID: {self._booking_id}, TripID: {self._trip_id}, PassengerID: {self._passenger_id}, BookingDate: {self._booking_date}, Status: {self._status})"



















































"""class Booking:
    def __init__(self, booking_id=None, trip_id=None, passenger_id=None, booking_date=None, status=None):
        self._booking_id = booking_id
        self._trip_id = trip_id
        self._passenger_id = passenger_id
        self._booking_date = booking_date
        self._status = status

    def get_booking_id(self):
        return self._booking_id

    def set_booking_id(self, booking_id):
        self._booking_id = booking_id

    def get_trip_id(self):
        return self._trip_id

    def set_trip_id(self, trip_id):
        self._trip_id = trip_id

    def get_passenger_id(self):
        return self._passenger_id

    def set_passenger_id(self, passenger_id):
        self._passenger_id = passenger_id

    def get_booking_date(self):
        return self._booking_date

    def set_booking_date(self, booking_date):
        self._booking_date = booking_date

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status """
