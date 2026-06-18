N = int(input())
A = list(map(int,input().split()))
stack = []
ans = []
for i, a in enumerate(A):
    T = (a,i+1)
    while stack and stack[-1] < T:
        stack.pop()
    if stack:
        ans.append(stack[-1][1])
    else:
        ans.append(-1)
    stack.append(T)

print(*ans)