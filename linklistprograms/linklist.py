__name__ = "__main__"
class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.val)
            current_node = current_node.next
