from collections import deque


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev, self.next = None, None

    def collapse(self):
        if self.prev is not None:
            self.prev.next = self.next

        if self.next is not None:
            self.next.prev = self.prev


class DoubleLinkedList:
    def __init__(self):
        self.__dummy_head = Node(0, 0)
        self.tail = None

    @property
    def head(self):
        return self.__dummy_head.next

    def apppend_left(self, node: Node):
        if self.head is None:
            self.tail = node
        else:
            self.head.prev = node

        node.next = self.head
        node.prev = self.__dummy_head
        self.__dummy_head.next = node

    def drop_right(self):
        if self.tail is None:
            return
        prev_tail = self.tail.prev
        if prev_tail is not None:
            prev_tail.next = None
        self.tail = prev_tail

    def __str__(self):
        result = "["
        node = self.head
        while node is not None:
            result += f"({node.key}, {node.value})"
            node = node.next
        result += "]"
        return result


class LRUCache:
    def __init__(self, limit=42):
        self.order = DoubleLinkedList()
        self.limit = limit
        self.cache = dict()

    def __update_lru(self, key):
        if key in self.cache:
            # collapse node
            pass

    def get(self, key):
        if key in self.cache:
            self.__update_lru(key)
            return self.cache[key]
        return -1

    def set(self, key, value):
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

dl = DoubleLinkedList()
node1 = Node(1, 1)
node2 = Node(2, 2)
node3 = Node(3, 3)

dl.apppend_left(node1)
dl.apppend_left(node2)
dl.apppend_left(node3)

node4 = Node(4, 4)
dl.apppend_left(node4)

print(dl)
