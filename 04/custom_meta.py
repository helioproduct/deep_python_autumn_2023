class CustomMeta(type):
    def __setattr__(cls, attribute, value):
        if not attribute.startswith("__"):
            attribute = "custom_" + attribute
        super().__setattr__(attribute, value)

    def __new__(cls, name, bases, dct):
        def custom_set(object, attribute, value):
            if not attribute.startswith("__"):
                attribute = "custom_" + attribute
            object.__dict__[attribute] = value

        new_dct = dict()
        for key in dct:
            new_key = key
            if not key.startswith("__"):
                new_key = "custom_" + key
            new_dct[new_key] = dct[key]

        new_dct["__setattr__"] = custom_set
        new_class = super().__new__(cls, name, bases, new_dct)

        return new_class


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def test_func(self) -> str:
        return f"{self}100"

    def __str__(self):
        return "Custom_by_metaclass"
