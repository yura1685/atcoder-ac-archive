from atcoder.dsu import DSU
from collections import defaultdict

N, M = map(int,input().split())

dsu = DSU(N+1)
g = []

for _ in range(M):
    u, v = map(int,input().split())
    dsu.merge(u,v)
    g.append((u,v))

d = defaultdict(int)

for u, v in g:
    d[dsu.leader(u)] += 1

ans = 0
p = dsu.groups()
for i in range(1,len(p)):
    if d[dsu.leader(p[i][0])] == len(p[i]) - 1:
        ans += 1

print(ans)