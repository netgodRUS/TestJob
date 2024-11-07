from collections import deque

class CircularBufferDeque:
    def __init__(self, size):
        self.buffer = deque(maxlen=size)

    def is_empty(self):
        return len(self.buffer) == 0

    def is_full(self):
        return len(self.buffer) == self.buffer.maxlen

    def enqueue(self, value):
        if self.is_full():
            self.buffer.popleft()
        self.buffer.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        return self.buffer.popleft()

    def __str__(self):
        return str(list(self.buffer))
