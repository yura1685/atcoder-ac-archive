from collections import Counter

N = int(input())
d = {}
for i in range(N):
    A, C = map(int,input().split())
    if C not in d:
        d[C] = A
    else:
        d[C] = min(d[C],A)

ans = 0
for i in d:
    ans = max(ans,d[i])
print(ans)