class Vehicle:
    def __init__(self, model=None, capacity=None, type=None, status=None, vehicle_id=None):
        self.model = model
        self.capacity = capacity
        self.type = type
        self.status = status
        self.vehicle_id = vehicle_id

    def __repr__(self):
        return f"Vehicle(ID: {self.vehicle_id}, Model: {self.model}, Capacity: {self.capacity}, Type: {self.type}, Status: {self.status})"
















"""
class Vehicle:
    def __init__(self, vehicle_id=None, model=None, capacity=None, type=None, status=None):
        self._vehicle_id = vehicle_id
        self._model = model
        self._capacity = capacity
        self._type = type
        self._status = status

    # Getters
    def get_vehicle_id(self):
        return self._vehicle_id

    def get_model(self):
        return self._model

    def get_capacity(self):
        return self._capacity

    def get_type(self):
        return self._type

    def get_status(self):
        return self._status

    # Setters
    def set_vehicle_id(self, vehicle_id):
        self._vehicle_id = vehicle_id

    def set_model(self, model):
        self._model = model

    def set_capacity(self, capacity):
        self._capacity = capacity

    def set_type(self, type):
        self._type = type

    def set_status(self, status):
        self._status = status

    def __str__(self):
        return f"Vehicle(ID: {self._vehicle_id}, Model: {self._model}, Capacity: {self._capacity}, Type: {self._type}, Status: {self._status})"

















#"""






"""class Vehicle:
    def __init__(self, vehicle_id=None, model=None, capacity=None, type=None, status=None):
        self._vehicle_id = vehicle_id
        self._model = model
        self._capacity = capacity
        self._type = type
        self._status = status

    def get_vehicle_id(self):
        return self._vehicle_id

    def set_vehicle_id(self, vehicle_id):
        self._vehicle_id = vehicle_id

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_capacity(self):
        return self._capacity

    def set_capacity(self, capacity):
        self._capacity = capacity

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status """
