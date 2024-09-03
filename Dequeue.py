class DeQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def isFull(self):
        return (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1)

    def isEmpty(self):
        return self.front == -1

    def insertFront(self, data):
        if self.isFull():
            return "Queue is full"
        if self.front == -1:
            self.front = self.rear = 0
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front -= 1
        self.queue[self.front] = data

    def insertRear(self, data):
        if self.isFull():
            return "Queue is full"
        if self.front == -1:
            self.front = self.rear = 0
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.queue[self.rear] = data

    def deleteFront(self):
        if self.isEmpty():
            return "Queue is empty"
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1
        return data

    def deleteRear(self):
        if self.isEmpty():
            return "Queue is empty"
        data = self.queue[self.rear]
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear -= 1
        return data


dq = DeQueue(5)
dq.insertFront(10)
dq.insertRear(20)
print("Deleted element from front", dq.deleteFront()) # Output: Deleted element from front 10
print("Deleted element from rear", dq.deleteRear())   # Output: Deleted element from rear 20
