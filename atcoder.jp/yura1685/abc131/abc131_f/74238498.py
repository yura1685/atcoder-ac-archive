from atcoder.dsu import DSU
from collections import defaultdict

N = int(input())
M = 10 ** 5
uf = DSU(2 * M + 1)
P = []
for _ in range(N):
    x, y = map(int, input().split())
    P.append((x, y))
    uf.merge(x, y + M)

E = defaultdict(int)
X = defaultdict(set)
Y = defaultdict(set)

for x, y in P:
    u = uf.leader(x)
    E[u] += 1
    X[u].add(x)
    Y[u].add(y)

ans = 0
for g in uf.groups():
    if len(g) == 1:
        continue
    u = uf.leader(g[0])
    ans += len(X[u]) * len(Y[u]) - E[u]

print(ans)