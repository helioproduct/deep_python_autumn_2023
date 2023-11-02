import re


class Email:
    __pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"

    def validate(self, email_str: str) -> bool:
        return bool(re.match(self.__pattern, email_str))

    def __init__(self, email_str):
        if self.validate(email_str):
            self.email = email_str

    def __set__():
        pass

    def __get__(self):
        print(self.email)


class Age:
    def __init__(self, min_age, max_age):
        self.min_age = min_age
        self.max_age = max_age

    def validate(self, age):
        return self.min_age <= age <= self.max_age


# class User:
#     num = PhoneNumber()
#     email = Email()
#     price = Age()

#     def __init__(self):
#         pass

email = Email("helioproduct.sync@gmail.com")
