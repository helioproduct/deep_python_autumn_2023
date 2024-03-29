import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def test_add(self):
        lst1 = CustomList([5, 1, 3, 7])
        lst2 = CustomList([1, 2, 7])
        lst4 = CustomList([2, 5])
        lst3 = CustomList([1])
        lst6 = CustomList([1])
        lst5 = [2, 5]

        self.assertEqual(list(lst1 + lst2), [6, 3, 10, 7])
        self.assertEqual(type(lst1 + lst2), CustomList)
        self.assertEqual(list(lst1), [5, 1, 3, 7])
        self.assertEqual(type(lst1), CustomList)
        self.assertEqual(list(lst2), [1, 2, 7])
        self.assertEqual(type(lst2), CustomList)

        self.assertEqual(list(lst3 + lst4), [3, 5])
        self.assertEqual(type(lst3 + lst4), CustomList)
        self.assertEqual(list(lst3), [1])
        self.assertEqual(type(lst3), CustomList)
        self.assertEqual(list(lst4), [2, 5])
        self.assertEqual(type(lst4), CustomList)

        self.assertEqual(list(lst6 + lst5), [3, 5])
        self.assertEqual(type(lst6 + lst5), CustomList)
        self.assertEqual(list(lst5), [2, 5])
        self.assertEqual(type(lst5), list)
        self.assertEqual(list(lst6), [1])
        self.assertEqual(type(lst6), CustomList)

        self.assertEqual(list(lst4 + [3, 5, 10]), [5, 10, 10])
        self.assertEqual(list(lst4 + [3]), [5, 5])
        self.assertEqual(list(lst4 + [3, 5]), [5, 10])

    def test_radd(self):
        lst4 = CustomList([2, 5])
        lst5 = [2, 5]
        lst6 = CustomList([1])

        self.assertEqual(list(lst5 + lst4), [4, 10])
        self.assertEqual(type(lst5 + lst4), CustomList)
        self.assertEqual(list(lst5), [2, 5])
        self.assertEqual(type(lst5), list)
        self.assertEqual(list(lst4), [2, 5])
        self.assertEqual(type(lst4), CustomList)

        self.assertEqual(
            list([1, 10, 100] + CustomList([2, 20, 200, 2000])), [3, 30, 300, 2000]
        )

        self.assertEqual(list(lst5 + lst6), [3, 5])
        self.assertEqual(type(lst5 + lst6), CustomList)

        self.assertEqual(list(lst5), [2, 5])
        self.assertEqual(list(lst6), [1])

        self.assertEqual(list(lst6 + lst4), [3, 5])
        self.assertEqual(type(lst6 + lst4), CustomList)
        self.assertEqual(list(lst6), [1])
        self.assertEqual(list(lst4), [2, 5])

    def test_sub(self):
        lst1 = CustomList([5, 1, 3, 7])
        lst2 = CustomList([1, 2, 7])
        lst3 = CustomList([1])
        lst4 = CustomList([2, 5])
        lst5 = [2, 5]
        lst6 = CustomList([1])

        self.assertEqual(list(lst1 - lst2), [4, -1, -4, 7])
        self.assertEqual(type(lst1 - lst2), CustomList)
        self.assertEqual(list(lst1), [5, 1, 3, 7])
        self.assertEqual(list(lst2), [1, 2, 7])

        self.assertEqual(list(lst3 - lst4), [-1, -5])
        self.assertEqual(type(lst3 - lst4), CustomList)
        self.assertEqual(list(lst3), [1])
        self.assertEqual(list(lst4), [2, 5])

        self.assertEqual(list(lst6 - lst5), [-1, -5])
        self.assertEqual(type(lst6 - lst5), CustomList)
        self.assertEqual(list(lst6), [1])
        self.assertEqual(lst5, [2, 5])

        self.assertEqual(
            list(CustomList([1, 2, 3]) - CustomList([3, 2, 1])), [-2, 0, 2]
        )
        self.assertEqual(list(lst2 - lst1), [-4, 1, 4, -7])
        self.assertEqual(list(lst2), [1, 2, 7])
        self.assertEqual(list(lst1), [5, 1, 3, 7])

        self.assertEqual(list(lst4 - [3, 5, 10]), [-1, 0, -10])
        self.assertEqual(list(lst4 - [3]), [-1, 5])
        self.assertEqual(list(lst4 - [3, 5]), [-1, 0])

    def test_rsub(self):
        lst4 = CustomList([2, 5])
        lst5 = [2, 5]
        lst6 = CustomList([1])
        lst2 = CustomList([1, 2, 3])

        self.assertEqual(list(lst5 - lst6), [1, 5])
        self.assertEqual(type(lst5 - lst6), CustomList)
        self.assertEqual(lst5, [2, 5])
        self.assertEqual(list(lst6), [1])

        self.assertEqual(list(lst5 - lst4), [0, 0])
        self.assertEqual(lst5, [2, 5])
        self.assertEqual(list(lst4), [2, 5])

        self.assertEqual(
            list([35, 15, 20] - CustomList([40, 20, 25, 5])), [-5, -5, -5, -5]
        )
        self.assertEqual(list(lst5 - lst2), [1, 3, -3])
        self.assertEqual(list(lst2), [1, 2, 3])

    def test_eq(self):
        lst1 = CustomList([5, 1, 3, 7])
        lst2 = CustomList([1, 2, 7])
        lst3 = CustomList([1])
        lst4 = CustomList([2, 5, 3])
        lst6 = CustomList([1])
        self.assertFalse(lst1 == lst2)
        self.assertFalse(lst3 == lst4)
        self.assertTrue(lst3 == lst6)
        self.assertTrue(lst2 == lst4)

    def test_ne(self):
        lst1 = CustomList([5, 1, 3, 7])
        lst2 = CustomList([1, 2, 7])
        lst3 = CustomList([1])
        lst4 = CustomList([2, 5, 3])
        lst6 = CustomList([1])

        self.assertTrue(lst1 != lst2)
        self.assertEqual(lst1, CustomList([5, 1, 3, 7]))
        self.assertEqual(lst2, CustomList([1, 2, 7]))

        self.assertTrue(lst3 != lst4)
        self.assertFalse(lst3 != lst6)
        # self.assertFalse(lst2 != lst4)

    def test_gt(self):
        lst1 = CustomList([5, 1, 3, 7])
        lst2 = CustomList([1, 2, 7])
        lst3 = CustomList([1])
        lst4 = CustomList([2, 5])
        lst6 = CustomList([1])

        self.assertTrue(lst1 > lst2)
        self.assertEqual(lst1, CustomList([5, 1, 3, 7]))
        self.assertEqual(lst2, CustomList([1, 2, 7]))

        self.assertTrue(lst4 > lst3)
        self.assertTrue(lst2 > lst6)

    def test_ge(self):
        lst1 = CustomList([5, 1, 3, 7])
        lst2 = CustomList([1, 2, 7])
        lst3 = CustomList([1])
        lst4 = CustomList([2, 5])
        lst6 = CustomList([1])

        self.assertTrue(lst1 >= lst2)
        self.assertEqual(lst1, CustomList([5, 1, 3, 7]))
        self.assertEqual(lst2, CustomList([1, 2, 7]))

        self.assertTrue(lst3 >= lst6)
        self.assertFalse(lst3 >= lst4)

    def test_lt(self):
        lst1 = CustomList([5, 1, 3, 7])
        lst2 = CustomList([1, 2, 7])
        lst3 = CustomList([1])
        lst4 = CustomList([2, 5])

        self.assertFalse(lst1 < lst2)
        self.assertEqual(lst1, CustomList([5, 1, 3, 7]))
        self.assertEqual(lst2, CustomList([1, 2, 7]))

        self.assertFalse(lst4 < lst3)
        self.assertTrue(lst3 < lst2)

    def test_le(self):
        lst1 = CustomList([5, 1, 3, 7])
        lst2 = CustomList([1, 2, 7])
        lst3 = CustomList([1])
        lst4 = CustomList([2, 5])
        lst6 = CustomList([1])

        self.assertTrue(lst2 <= lst1)
        self.assertEqual(lst1, CustomList([5, 1, 3, 7]))
        self.assertEqual(lst2, CustomList([1, 2, 7]))

        self.assertFalse(lst4 <= lst3)
        self.assertTrue(lst3 <= lst6)


if __name__ == "__main__":
    unittest.main()
