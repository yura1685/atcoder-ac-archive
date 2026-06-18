from collections import deque

N, M = map(int,input().split())
S = input()
C = list(map(int,input().split()))

d = [deque() for _ in range(M+1)]

for i in range(N):
    d[C[i]].append(S[i])

for i in range(M+1):
    if d[i]:
        n = d[i].pop()
        d[i].appendleft(n)

ans = ''
for c in C:
    n = d[c].popleft()
    ans += n

print(ans)