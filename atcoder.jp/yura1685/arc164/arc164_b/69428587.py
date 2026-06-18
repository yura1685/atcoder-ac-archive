from atcoder.dsu import DSU

N, M = map(int,input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

c = list(map(int,input().split()))

uf = DSU(N)

for u in range(N):
    for v in g[u]:
        if c[u] + c[v] == 1:
            uf.merge(u, v)

for G in uf.groups():
    for u in G:
        for v in g[u]:
            if c[u] == c[v] and uf.same(u,v):
                exit(print('Yes'))

print('No')