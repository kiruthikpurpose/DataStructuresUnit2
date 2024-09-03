class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            return "Queue Underflow"
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None
        return temp.data

    def front_element(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Front element is", queue.front_element()) # Output: Front element is 10
print("Dequeued element is", queue.dequeue()) # Output: Dequeued element is 10
