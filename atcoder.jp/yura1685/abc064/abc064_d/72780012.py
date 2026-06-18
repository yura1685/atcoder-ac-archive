N = int(input())
S = input()
stack = []
for s in S:
    if not stack or s == '(':
        stack.append(s)
    else:
        if stack[-1] == '(':
            stack.pop()
        else:
            stack.append(s)

n, m = stack.count(')'), stack.count('(')
print('('*n+S+')'*m)