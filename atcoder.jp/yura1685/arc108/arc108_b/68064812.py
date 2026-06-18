N = int(input())
S = input()
stack = []

for s in S:
    if s != 'x':
        stack.append(s)
    else:
        if len(stack) >= 2 and stack[-2:] == ['f','o']:
            stack.pop(); stack.pop()
        else:
            stack.append(s)

print(len(stack))