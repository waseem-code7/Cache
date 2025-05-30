from typing import Dict

from DoublyLinkedList import DoublyLinkedList, Node


class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key} : {self.value}"


class LRU:

    def __init__(self, cap):
        self.cap = cap
        self.dll = DoublyLinkedList()
        self.map: Dict[int, Node] = dict()
        self.size = 0

    def add(self, key, value) -> Node | None:
        data = Data(key, value)
        if self.cap == self.size:
            removed = self.dll.remove_last()

            if removed is None:
                return None

            del self.map[removed.data.key]
            node = self.dll.add_first(data)
            self.map[key] = node
            return node
        else:
            node = self.dll.add_first(data)
            self.map[key] = node
            self.size += 1
            return node

    def replace(self, key, value) -> Node:
        node = self.map.get(key)
        node.data.value = value
        self.dll.move_to_first(node)
        return node

    def set(self, key, value):
        if key in self.map:
            return self.replace(key, value)
        else:
            return self.add(key, value)

    def get(self, key):
        if key in self.map:
            node = self.map.get(key)
            self.dll.move_to_first(node)
            return node.data.value
        return float("-inf")

    def remove(self, key) -> Node | None:
        if key in self.map:
            node = self.map.get(key)
            self.dll.move_to_first(node)
            removed = self.dll.remove_first()


            if removed is None:
                return None
            self.size -= 1
            del self.map[removed.data.key]
            return removed

        return None

    def remove_least_recently_used(self) -> Node | None:
        if self.size == 0:
            return None
        node = self.dll.remove_last()
        del self.map[node.data.key]
        self.size -= 1
        return node

    def print(self):
        if self.size > 0:
            self.dll.print()

# TESTS
# lru = LRU(2)
# lru.add(1, 1)
# lru.print()
# lru.add(2,2)
# lru.print()
# lru.get(1)
# lru.print()
# lru.add(3, 3)
# lru.print()
# lru.get(2)
# lru.print()
# lru.add(4, 4)
# lru.print()
# lru.get(1)
# lru.print()
# lru.get(3)
# lru.print()
# lru.get(4)
# lru.print()




