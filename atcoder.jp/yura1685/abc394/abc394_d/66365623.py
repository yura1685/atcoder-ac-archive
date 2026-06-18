S = input()
stack = []
for s in S:
    if s in '([<':
        stack.append(s)
    elif s == ')':
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            print('No')
            exit()
    elif s == ']':
        if stack and stack[-1] == '[':
            stack.pop()
        else:
            print('No')
            exit()
    elif s == '>':
        if stack and stack[-1] == '<':
            stack.pop()
        else:
            print('No')
            exit()
print('Yes' if not stack else 'No')