class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, obj):
        self.queue.append(obj)

    def dequeue(self):
        if self.empty():
            raise Exception("Queue is empty")
        elem = self.queue[0]
        self.queue = self.queue[1:]
        return elem

    def peek(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.queue[0]
    
    def contains(self, obj):
        for item in self.queue:
            if obj == item:
                return True
        return False
    
    def size(self):
        return len(self.queue)

    def empty(self):
        return len(self.queue) == 0
