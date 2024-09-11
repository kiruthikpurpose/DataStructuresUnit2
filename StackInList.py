stack = []

def push():
    element = int(input("Enter the element to push: "))
    stack.append(element)

def pop():
    if not is_empty():
        print("Popped element:", stack.pop())
    else:
        print("Stack is empty")

def peek():
    if not is_empty():
        print("Top element:", stack[-1])
    else:
        print("Stack is empty")

def is_empty():
    return len(stack) == 0

def size():
    print("Size of the stack:", len(stack))

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
