import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_from_example(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k3", "val3")

        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), "val1")

    def test_cache_set_and_get(self):
        cache = LRUCache(2)
        cache.set(1, 1)
        cache.set(2, 2)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)

    def test_cache_eviction(self):
        cache = LRUCache(2)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        self.assertIsNone(cache.get(1))
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), 3)

    def test_cache_update(self):
        cache = LRUCache(2)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(1, 10)
        self.assertEqual(cache.get(1), 10)
        cache.set(3, 3)
        self.assertIsNone(cache.get(2))

    def test_cache_over_capacity(self):
        cache = LRUCache(1)
        cache.set(1, 1)
        cache.set(2, 2)
        self.assertIsNone(cache.get(1))
        self.assertEqual(cache.get(2), 2)

    def test_cache_removal(self):
        cache = LRUCache(2)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)
        self.assertIsNone(cache.get(1))
        self.assertIsNone(cache.get(2))
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)


if __name__ == "__main__":
    unittest.main()
