from collections import deque


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev, self.right = None, None

    def collapse(self):
        if self.prev is not None:
            print("hello")
            self.prev.next = self.next

        if self.next is not None:
            print("hello2")
            self.next.prev = self.prev


class DoubleLinkedList:
    def __init__(self, key, value):
        self.head = Node(key, value)

    def appendleft(self, node: Node):
        node.next = self.head

    def dropright(self):
        pass


class LRUCache:
    def __init__(self, limit=42):
        # Left is LRU
        self.order = deque()
        self.limit = limit
        self.cache = dict()

    def update_lru(self, key):
        pass

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        return -1

    def set(self, key, value):
        if key in self.cache:
            pass


# cache = LRUCache(2)

# cache.set("k1", "val1")
# cache.set("k2", "val2")

# assert cache.get("k3") is None
# assert cache.get("k1") == "val1"
# assert cache.get("k2") == "val2"

# cache.set("k3", "val3")

# assert cache.get("k3") == "val3"
# assert cache.get("k2") is None
# assert cache.get("k1") == "val1"

# cache["k1"] = "val1"
# print(cache["k3"])


left = Node(5, 5)
left.next = Node(5, 5)
left.next.next = Node(6, 6)

left.next.collapse()

print(left.next.value)
