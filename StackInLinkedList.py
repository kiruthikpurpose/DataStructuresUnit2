class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

top = None

def push():
    global top
    element = int(input("Enter the element to push: "))
    new_node = Node(element)
    new_node.next = top
    top = new_node

def pop():
    global top
    if is_empty():
        print("Stack is empty")
    else:
        print("Popped element:", top.data)
        top = top.next

def peek():
    if is_empty():
        print("Stack is empty")
    else:
        print("Top element:", top.data)

def is_empty():
    return top is None

def size():
    current = top
    count = 0
    while current:
        count += 1
        current = current.next
    print("Size of the stack:", count)

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Size")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        size()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
