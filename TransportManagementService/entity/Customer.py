class Customer:
    def __init__(self, customer_id=None, username=None, password=None, first_name=None, gender=None, age=None, email=None, phone_number=None):
        self._customer_id = customer_id
        self._username = username
        self._password = password
        self._first_name = first_name
        self._gender = gender
        self._age = age
        self._email = email
        self._phone_number = phone_number

    def get_customer_id(self):
        return self._customer_id

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_first_name(self):
        return self._first_name

    def get_gender(self):
        return self._gender

    def get_age(self):
        return self._age

    def get_email(self):
        return self._email

    def get_phone_number(self):
        return self._phone_number

    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_gender(self, gender):
        self._gender = gender

    def set_age(self, age):
        self._age = age

    def set_email(self, email):
        self._email = email

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def __str__(self):
        return f"Customer(ID: {self._customer_id}, Username: {self._username}, Email: {self._email})"
