from collections import defaultdict
N, K = map(int,input().split())
S = input()
d = defaultdict(int)
M = 0

for i in range(N-K+1):
    T = S[i:i+K]
    d[T] += 1

M = max(d.values())
ans = []
for t in d:
    if d[t] == M:
        ans.append(t)

ans.sort()
print(M)
print(*ans)