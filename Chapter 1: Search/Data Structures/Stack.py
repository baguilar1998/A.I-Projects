class Stack:

    def __init__(self):
        self.stack = []

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.stack[-1]

    def contains(self,obj):
        for item in self.stack:
            if item == obj:
                return True
        return False
    
    def size(self):
        return len(self.stack)

    def empty(self):
        return len(self.stack) == 0
