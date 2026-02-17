from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if len(self.items) == 0:
            raise IndexError("Pop: Stack is empty")
        return self.items.pop()
    
    def peek(self):
        if len(self.items) == 0:
            raise IndexError("Peek: Stack is empty")
        return self.items[-1]