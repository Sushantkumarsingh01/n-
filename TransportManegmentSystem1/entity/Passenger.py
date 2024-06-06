class Passenger:
    def __init__(self, passenger_id=None, name=None, email=None, phone_number=None):
        self._passenger_id = passenger_id
        self._name = name
        self._email = email
        self._phone_number = phone_number

    # Getters
    def get_passenger_id(self):
        return self._passenger_id

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_phone_number(self):
        return self._phone_number

    # Setters
    def set_passenger_id(self, passenger_id):
        self._passenger_id = passenger_id

    def set_name(self, name):
        self._name = name

    def set_email(self, email):
        self._email = email

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def __str__(self):
        return f"Passenger(ID: {self._passenger_id}, Name: {self._name}, Email: {self._email}, PhoneNumber: {self._phone_number})"




























"""class Passenger:
    def __init__(self, passenger_id=None, first_name=None, gender=None, age=None, email=None, phone_number=None):
        self._passenger_id = passenger_id
        self._first_name = first_name
        self._gender = gender
        self._age = age
        self._email = email
        self._phone_number = phone_number

    def get_passenger_id(self):
        return self._passenger_id

    def set_passenger_id(self, passenger_id):
        self._passenger_id = passenger_id

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        self._gender = gender

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number """
