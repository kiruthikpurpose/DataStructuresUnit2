class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def isEmpty(self):
        return self.front == -1

    def enqueue(self, data):
        if self.isFull():
            return "Queue is full"
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return data


cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
print("Dequeued element is", cq.dequeue()) # Output: Dequeued element is 10
