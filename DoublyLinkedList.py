class Node:

    def __init__(self, data: any):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = Node(float("-inf"))
        self.tail = Node(float("inf"))
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_first(self, data: any) -> Node:
        node = Node(data)
        first_node: Node = self.head.next

        self.head.next = node
        node.next = first_node
        first_node.prev = node
        node.prev = self.head
        return node

    def add_last(self, data: any) -> Node:
        node = Node(data)
        last_node = self.tail.prev

        last_node.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = last_node
        return node

    def remove_first(self):
        if self.head.next == self.tail:
            return

        node_to_rem = self.head.next

        self.head.next = node_to_rem.next
        node_to_rem.next.prev = self.head

        node_to_rem.next = None
        node_to_rem.prev = None

        return node_to_rem


    def remove_last(self):
        if self.head.next == self.tail:
            return

        node_to_rem = self.tail.prev

        self.tail.prev = node_to_rem.prev
        node_to_rem.prev.next = self.tail

        node_to_rem.next = None
        node_to_rem.prev = None

        return node_to_rem

    def move_to_first(self, node: Node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node

    def print(self):
        if self.head.next == self.tail:
            print("Empty")
            print([])
        node = self.head.next

        while node != self.tail:
            print(node.data, end=" -> ")
            node = node.next
        print()


