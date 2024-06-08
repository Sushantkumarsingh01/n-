class VehicleNotFoundException(Exception):
    def __init__(self):
        super().__init__("Vehicle not found.")









"""class VehicleNotFoundException(Exception):
    def __init__(self, message="Vehicle not found"):
        self.message = message
        super().__init__(self.message) """
