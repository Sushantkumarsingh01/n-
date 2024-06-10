
class BookingNotFoundException(Exception):
    def __init__(self):
        super().__init__("Booking not found.")

