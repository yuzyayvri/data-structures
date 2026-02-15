class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node
        
    def traverse(self):
        current_node = self.head
        while current_node:
            print   (current_node.data)
            current_node = current_node.next