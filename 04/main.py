class MyDecriptor:
    def __get__(self, obj, objtype):
        print("")


print(type(MyDecriptor))
