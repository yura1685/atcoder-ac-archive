S = input()
stack = []
l = 0
for s in S:
    if s != 'C':
        stack.append(s)
        l += 1
    else:
        if l >= 2 and stack[-2:] == ['A','B']:
            stack.pop()
            stack.pop()
            l -= 2
        else:
            stack.append(s)
print(''.join(stack))