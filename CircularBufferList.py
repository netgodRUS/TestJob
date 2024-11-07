class CircularBufferList:
    def __init__(self, size):
        self.buffer = [None] * size
        self.size = size
        self.start = 0
        self.end = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Buffer is full")
        self.buffer[self.end] = value
        self.end = (self.end + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        value = self.buffer[self.start]
        self.buffer[self.start] = None
        self.start = (self.start + 1) % self.size
        self.count -= 1
        return value

    def __str__(self):
        return str([self.buffer[(self.start + i) % self.size] for i in range(self.count)])
