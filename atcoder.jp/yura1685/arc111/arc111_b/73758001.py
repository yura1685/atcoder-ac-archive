from atcoder.dsu import DSU

N = int(input())
g = [[] for _ in range(400000)]
uf = DSU(400000)
for _ in range(N):
    a, b = map(int,input().split())
    a, b = a-1, b-1
    uf.merge(a, b)
    g[a].append(b)
    g[b].append(a)
E = [len(g[i]) for i in range(400000)]

ans = 400000

for g in uf.groups():
    e = 0
    for u in g:
        e += E[u]
    e //= 2
    if e + 1 == len(g):
        ans -= 1

print(ans)