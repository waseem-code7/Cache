from typing import Dict, List, Union
from DoublyLinkedList import Node
from LRU import LRU


class LFU:

    def __init__(self, cap):
        self.frequency: Dict[int, LRU] = dict()
        self.map: Dict[int, List[Union[Node, int, None]]] = dict()
        self.min_frequency = 0
        self.cap = cap
        self.size = 0

    def add(self, key, value):
        if self.cap == self.size:
            lru = self.frequency.get(self.min_frequency)
            removed = lru.remove_least_recently_used()
            self.size -= 1
            del self.map[removed.data.key]
            return self.add(key, value)
        else:
            if 1 in self.frequency:
                node = self.frequency.get(1).set(key, value)
            else:
                self.frequency[1] = LRU(float("inf"))
                node = self.frequency.get(1).set(key, value)
            self.map[key] = [node, 1]
            self.min_frequency = 1
            self.size += 1
            return node

    def replace(self, key, value):
        node, freq = self.map.get(key)
        node.data.value = value
        self.frequency.get(freq).remove(key)
        del self.map[key]

        if (freq + 1) in self.frequency:
            new_node = self.frequency.get(freq + 1).set(key, value)
        else:
            self.frequency[freq + 1] = LRU(float("inf"))
            new_node = self.frequency.get(freq + 1).set(key, value)

        self.map[key] = [new_node, freq + 1]
        if self.frequency.get(freq).size == 0 and self.min_frequency == freq:
            del self.frequency[freq]
            self.min_frequency = freq + 1

        return new_node

    def set(self, key, value):
        if key in self.map:
            return self.replace(key, value)
        else:
            return self.add(key, value)

    def get(self, key):
        if key in self.map:
            curr_node, freq = self.map.get(key)
            value = curr_node.data.value
            self.replace(key, value)
            return value

    def print(self):
        print(f"MIN FREQ :: {self.min_frequency}")
        for key, dll in self.frequency.items():
            print(f"{key} ::::", end=" ")
            dll.print()
            print()

    def set_next_min_frequency(self):
        freq = self.min_frequency
        reset_success = False

        while True:
            if self.frequency.get(freq).size == 0:
                freq += 1
            else:
                self.min_frequency = freq
                reset_success = True
                break

        if not reset_success:
            self.__init__(self.cap)

    # Remove is not O(1) because min_frequency needs to be reset to correct value on deletion
    def remove(self, key):
        if key not in self.map:
            return None

        if self.size == 1:
            # reset instance
            self.__init__(self.cap)
            return

        node, freq = self.map.get(key)
        if freq == self.min_frequency:
            self.frequency.get(freq).remove(key)
            if self.frequency.get(freq).size == 0:
                self.set_next_min_frequency()
        else:
            self.frequency.get(freq).remove(key)

        if self.size > 0:
            self.size -= 1
            del self.map[key]


# TESTS
# lfu = LFU(4)
# lfu.set(1,2)
# lfu.set(2,3)
# lfu.set(3,4)
# lfu.set(4,5)
# lfu.get(3)
# lfu.get(3)
# lfu.get(3)
# lfu.get(2)
# lfu.get(2)
# lfu.get(4)
# lfu.get(4)
# lfu.remove(1)
# lfu.set(4, 6)
# lfu.set(7, 6)
# lfu.print()

