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

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def infix_to_postfix(expression):
    stack = Stack()
    result = ''
    for char in expression:
        if char.isalnum():
            result += char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while (not stack.isEmpty()) and stack.peek() != '(':
                result += stack.pop()
            stack.pop()
        else:
            while (not stack.isEmpty()) and precedence(char) <= precedence(stack.peek()):
                result += stack.pop()
            stack.push(char)
    while not stack.isEmpty():
        result += stack.pop()
    return result


expr = "a+b*(c^d-e)^(f+g*h)-i"
print("Postfix expression is:", infix_to_postfix(expr))
