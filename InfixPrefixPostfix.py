def prec(c):
    if c == '^':
        return 2
    elif c == '/' or c == '*':
        return 1
    elif c == '+' or c == '-':
        return 0
    else:
        return -1

def infix_to_postfix(s):
    postfix = []
    stack = []
    
    for c in s:
        if c.isalnum():
            postfix.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and (prec(c) < prec(stack[-1]) or (prec(c) == prec(stack[-1]) and c != '^')):
                postfix.append(stack.pop())
            stack.append(c)
    
    while stack:
        postfix.append(stack.pop())
    
    return "".join(postfix)

def pre_to_post(pre):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    
    for c in reversed(pre):
        if c not in operators:
            stack.append(c)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 + op2 + c)
    
    return stack[-1]

def pre_to_in(pre):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    
    for c in reversed(pre):
        if c not in operators:
            stack.append(c)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f'({op1}{c}{op2})')
    
    return stack[-1]

def post_to_pre(post):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    
    for c in post:
        if c not in operators:
            stack.append(c)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(c + op1 + op2)
    
    return stack[-1]

def post_to_in(post):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    
    for c in post:
        if c not in operators:
            stack.append(c)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(f'({op1}{c}{op2})')
    
    return stack[-1]

def infix_to_prefix(s):
    s = s[::-1]
    
    for i in range(len(s)):
        if s[i] == '(':
            s = s[:i] + ')' + s[i+1:]
        elif s[i] == ')':
            s = s[:i] + '(' + s[i+1:]

    stack = []
    prefix = []
    
    for c in s:
        if c.isalnum():
            prefix.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                prefix.append(stack.pop())
            stack.pop()
        else:
            while stack and (prec(c) < prec(stack[-1]) or (prec(c) == prec(stack[-1]) and c != '^')):
                prefix.append(stack.pop())
            stack.append(c)

    while stack:
        prefix.append(stack.pop())

    return "".join(prefix[::-1])

# Example usage:
s = input("Enter infix expression: ")
print("Infix to Postfix:", infix_to_postfix(s))
pre = input("Enter Prefix expression: ")
print("Prefix to Postfix:", pre_to_post(pre))
print("Prefix to Infix:", pre_to_in(pre))
post = input("Enter Postfix expression: ")
print("Postfix to Prefix:", post_to_pre(post))
print("Postfix to Infix:", post_to_in(post))
