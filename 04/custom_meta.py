class CustomMeta(type):
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

        return super().__new__(cls, name, bases, new_dct)
