from atcoder.dsu import DSU

N, M = map(int,input().split())
graph = DSU(N+1)
g = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int,input().split())
    graph.merge(u,v)
    g[u].append(v)
    g[v].append(u)

c = list(graph.groups())
n = len(c)

ans = 0
for i in range(1,n):
    hoge = 0
    for u in c[i]:
        hoge += len(g[u])
    if len(c[i]) != hoge//2:
        print('No')
        exit()
print('Yes')