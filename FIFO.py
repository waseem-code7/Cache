from typing import Dict

from DoublyLinkedList import Node, DoublyLinkedList

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key} : {self.value}"


class FIFO:
    def __init__(self, cap):
        self.map: Dict[int, Node] = dict()
        self.dll = DoublyLinkedList()
        self.cap = cap
        self.size = 0

    def add(self, key, value) -> Node | None:
        if self.cap == self.size:
            node = self.dll.remove_first()
            del self.map[node.data.key]
            self.size -= 1

        data = Data(key, value)
        node = self.dll.add_last(data)
        self.size += 1
        self.map[key] = node
        return node

    def get(self, key) -> any:
        if key not in self.map:
            return None
        return self.map.get(key).data.value

    def replace(self, key, value) -> Node | None:
        node = self.map.get(key)
        node.data.value = value
        return node


    def set(self, key, value) -> Node | None:
        if key in self.map:
            return self.replace(key, value)
        else:
            return self.add(key, value)

    def remove(self, key) -> Node | None:
        if key not in self.map:
            return None

        node = self.map.get(key)
        self.dll.move_to_first(node)
        self.dll.remove_first()
        self.size -= 1
        del self.map[key]

        return node

    def print(self):
        self.dll.print()

# TESTS
# fifo = FIFO(3)
# fifo.add(1, 2)
# fifo.add(2, 4)
# fifo.add(3, 4)
# fifo.add(4, 5)
# fifo.print()
# print(fifo.get(1))
# print(fifo.get(2))
# fifo.remove(3)
# fifo.print()



