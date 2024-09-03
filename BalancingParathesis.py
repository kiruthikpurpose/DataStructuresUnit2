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

def are_brackets_balanced(expr):
    stack = Stack()
    for char in expr:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.isEmpty():
                return False
            top_char = stack.pop()
            if not ((top_char == '(' and char == ')') or 
                    (top_char == '{' and char == '}') or 
                    (top_char == '[' and char == ']')):
                return False
    return stack.isEmpty()


expr = "{[()()]}"
print("Balanced" if are_brackets_balanced(expr) else "Not Balanced")
