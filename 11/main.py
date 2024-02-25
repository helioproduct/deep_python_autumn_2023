class Person:
    def __init__(self):
        pass

    def __del__(self):
        print(f"__del__ for Person")


person1 = Person()
person2 = Person()

del person2, person1
