class CustomList(list):
    def __add__(self, other):
        sum = self if len(self) > len(other) else other
        for i in range(min(len(self), len(other))):
            sum[i] = self[i] + other[i]
        return sum


first = CustomList([5, 1, 3, 7])
second = CustomList([1, 2, 7])
second = [1, 2, 7]
result = first + second

print(result)
print(type(result))
