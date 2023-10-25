class CustomList(list):
    def __add__(self, other):
        sum = self if len(self) > len(other) else other
        for i in range(min(len(self), len(other))):
            sum[i] = self[i] + other[i]
        return sum

    def __sub__(self, other):
        sum = self if len(self) > len(other) else other
        for i in range(min(len(self), len(other))):
            sum[i] = self[i] - other[i]
        return sum

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __nq__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __str__(self):
        return f"{list(self)} {sum(self)}"


# first = CustomList([5, 1, 3, 7])
# second = CustomList([1, 2, 7])


# second = [1, 2, 7]
# result = CustomList([2, 5]) + CustomList([1])

print(CustomList([1, 2, 5]))
