
class BookingNotFoundException(Exception):
    def __init__(self):
        super().__init__("Booking not found.")





"""class BookingNotFoundException(Exception):
    def __init__(self, message="Booking not found"):
        self.message = message
        super().__init__(self.message) """
