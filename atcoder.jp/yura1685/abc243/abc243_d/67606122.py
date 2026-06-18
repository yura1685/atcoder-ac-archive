N, X = map(int,input().split())
S = list(input())
stack = []

for s in S:
    if s == 'U' and stack and stack[-1] != 'U':
        stack.pop()
    else:
        stack.append(s)

ans = X
for s in stack:
    if s == 'U':
        ans //= 2
    elif s == 'L':
        ans = 2*ans
    else:
        ans = 2*ans + 1

print(ans)