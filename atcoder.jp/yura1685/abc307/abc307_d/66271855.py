N = int(input())
S = input()

stack = []
left  = 0

for i in range(N):
    s = S[i]
    if s != ')':
        stack.append(s)
        if s == '(':
            left += 1
    else:
        if left == 0:
            stack.append(s)
        else:
            while stack[-1] != '(':
                stack.pop()
            stack.pop()
            left -= 1
print(''.join(stack))