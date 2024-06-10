class VehicleNotFoundException(Exception):
    def __init__(self):
        super().__init__("Vehicle not found.")


