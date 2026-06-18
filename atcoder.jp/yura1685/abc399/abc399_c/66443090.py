from atcoder.dsu import DSU

N, M = map(int,input().split())

graph = DSU(N+1)
g = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int,input().split())
    graph.merge(u,v)
    g[u].append(v)
    g[v].append(u)

ans = 0
for i in graph.groups():
    if len(i) > 1:
        hoge = 0
        for u in i:
            hoge += len(g[u])
        ans += hoge//2 - (len(i)-1)

print(ans)