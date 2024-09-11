class Stack:
    def __init__(self, capacity):
        self.stack = [None] * capacity
        self.capacity = capacity
        self.top = -1

    def push(self):
        if self.top == self.capacity - 1:
            print("Stack overflow")
        else:
            element = int(input("Enter the element to push: "))
            self.top += 1
            self.stack[self.top] = element

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
        else:
            print("Popped element:", self.stack[self.top])
            self.stack[self.top] = None
            self.top -= 1

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Top element:", self.stack[self.top])

    def is_empty(self):
        return self.top == -1

    def size(self):
        print("Size of the stack:", self.top + 1)

    def display(self):
        print("Stack:", self.stack)

stack = Stack(5)

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Size")
    print("5. Display")
    print("6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        stack.push()
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.peek()
    elif choice == 4:
        stack.size()
    elif choice == 5:
        stack.display()
    elif choice == 6:
        break
    else:
        print("Invalid choice")
