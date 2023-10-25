class CustomList(list):
    def __add__(self, other):
        sum = self.copy() if len(self) > len(other) else other.copy()
        for i in range(min(len(self), len(other))):
            sum[i] = self[i] + other[i]
        return CustomList(sum)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        negative_other = CustomList([(-1) * x for x in other])
        return self + negative_other

    def __rsub__(self, other):
        return CustomList(other) - self

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
