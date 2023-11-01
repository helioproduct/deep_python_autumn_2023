class CustomMeta(type):
    def __new__(cls, name, bases, dct):
        def custom_set(object, attribute, value):
            print("hello")

            if not attribute.startswith("__"):
                attribute = "custom_" + attribute

            object.__dict__[attribute] = value
            # setattr(object, attribute, value)

        new_dct = dict()
        for key in dct:
            new_key = key
            if not key.startswith("__"):
                new_key = "custom_" + key
            new_dct[new_key] = dct[key]

        new_dct["__setattr__"] = custom_set

        return super().__new__(cls, name, bases, new_dct)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


# inst.__set__("test", "100")


# for x in dir(inst):
#     print(x)


# assert CustomClass.custom_x == 50
# CustomClass.x  # ошибка

# inst = CustomClass()
# assert inst.custom_x == 50
# assert inst.custom_val == 99
# assert inst.custom_line() == 100
# assert str(inst) == "Custom_by_metaclass"

# inst.x  # ошибка
# inst.val  # ошибка
# inst.line()  # ошибка
# inst.yyy  # ошибка

# inst.dynamic = "added later"
# assert inst.custom_dynamic == "added later"
# inst.dynamic  # ошибка
