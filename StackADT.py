class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            return "Stack Underflow"
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.top.data


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Top element is", stack.peek()) # Output: Top element is 30
print("Popped element is", stack.pop()) # Output: Popped element is 30
