from atcoder.dsu import DSU
from sys import setrecursionlimit
setrecursionlimit(10**8)

N = int(input())
uf = DSU(N)
g = [[] for _ in range(N)]

for _ in range(N):
    u, v = map(int,input().split())
    u, v = u-1, v-1
    if uf.same(u, v):
        S, T = u, v
    else:
        uf.merge(u, v)
    g[u].append(v)
    g[v].append(u)

check = [0] * N; check[S] = 1
path = [S]
cycle = set()

def dfs(u):
    for v in g[u]:
        if check[v]:
            continue
        check[v] = 1
        path.append(v)
        if v == T:
            for p in path:
                cycle.add(p)
        dfs(v)
        path.pop()

dfs(S)

pare = [i for i in range(N)]

def dfs2(u,p):
    for v in g[u]:
        if pare[v] == p or v in cycle:
            continue
        pare[v] = p
        dfs2(v,p)

for p in cycle:
    dfs2(p,p)

Q = int(input())
for _ in range(Q):
    x, y = map(int,input().split())
    print('Yes' if pare[x-1] == pare[y-1] else 'No')