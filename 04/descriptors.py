import re


class EmailDescriptor:
    def __get__(self, instance, owner):
        return instance._email

    def __set__(self, instance, value):
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value):
            raise ValueError("Invalid email address")
        instance._email = value

    def __delete__(self, instance):
        del instance._email


class AgeDescriptor:
    def __get__(self, instance, owner):
        return instance._age

    def __set__(self, instance, value):
        if not (0 <= value <= 120):
            raise ValueError("Invalid age")
        instance._age = value

    def __delete__(self, instance):
        del instance._age


class PhoneNumberDescriptor:
    def __get__(self, instance, owner):
        return instance._phone_number

    def __set__(self, instance, value):
        if not re.match(r"^\d{10}$", value):
            raise ValueError("Invalid phone number")
        instance._phone_number = value

    def __delete__(self, instance):
        del instance._phone_number


class MyClass:
    email = EmailDescriptor()

    def __init__(self, email):
        self.email = email
