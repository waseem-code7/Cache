from DoublyLinkedList import DoublyLinkedList


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
        self.map = dict()
        self.size = 0

    def add(self, key, value):
        data = Data(key, value)
        if self.cap == self.size:
            removed = self.dll.remove_last()
            del self.map[removed.data.key]
            node = self.dll.add_first(data)
            self.map[key] = node
        else:
            node = self.dll.add_first(data)
            self.map[key] = node
            self.size += 1

    def replace(self, key, value):
        node = self.map.get(key)
        node.data.value = value
        self.dll.move_to_first(node)

    def set(self, key, value):
        if key in self.map:
            self.replace(key, value)
        else:
            self.add(key, value)

    def get(self, key):
        if key in self.map:
            node = self.map.get(key)
            self.dll.move_to_first(node)
            return node.data.value
        return float("-inf")

    def print(self):
        if self.size > 0:
            self.dll.print()

# TESTS
lru = LRU(2)
lru.add(1, 1)
lru.print()
lru.add(2,2)
lru.print()
lru.get(1)
lru.print()
lru.add(3, 3)
lru.print()
lru.get(2)
lru.print()
lru.add(4, 4)
lru.print()
lru.get(1)
lru.print()
lru.get(3)
lru.print()
lru.get(4)
lru.print()




