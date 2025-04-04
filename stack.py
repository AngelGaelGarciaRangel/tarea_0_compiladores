class Stack:
    def __init__(self):
        self.stck = []
    
    def push(self, item):
        self.stck.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stck.pop()
        else:
            raise IndexError("pop from empty stack")
    
    def size(self):
        return len(self.stck)

    def is_empty(self):
        return self.size() == 0
    
    def peek(self):
        if not self.is_empty():
            return self.stck[-1]
        else:
            raise IndexError("peek from empty stack")