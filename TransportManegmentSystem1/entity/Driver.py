class Driver:
    def __init__(self, driver_id=None, name=None, license_number=None, phone_number=None):
        self._driver_id = driver_id
        self._name = name
        self._license_number = license_number
        self._phone_number = phone_number

    # Getters
    def get_driver_id(self):
        return self._driver_id

    def get_name(self):
        return self._name

    def get_license_number(self):
        return self._license_number

    def get_phone_number(self):
        return self._phone_number

    # Setters
    def set_driver_id(self, driver_id):
        self._driver_id = driver_id

    def set_name(self, name):
        self._name = name

    def set_license_number(self, license_number):
        self._license_number = license_number

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def __str__(self):
        return f"Driver(ID: {self._driver_id}, Name: {self._name}, LicenseNumber: {self._license_number}, PhoneNumber: {self._phone_number})"
