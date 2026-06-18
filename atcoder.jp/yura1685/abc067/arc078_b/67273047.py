from collections import deque
from atcoder.dsu import DSU

N = int(input())
g = [[] for _ in range(N+1)]
edge = []
for _ in range(N-1):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
    edge.append((a,b))

dis = [float('inf')]*(N+1)
dis[1] = 0
d = deque([1])
while d:
    u = d.popleft()
    if u == N:
        break
    for v in g[u]:
        if dis[v] > dis[u]:
            dis[v] = dis[u] + 1
            d.append(v)

Nto1 = [N]
while True:
    u = Nto1[-1]
    if u == 1:
        break
    for v in g[u]:
        if dis[v] == dis[u]-1:
            Nto1.append(v)
            break

n = len(Nto1)
u, v = Nto1[n//2-1], Nto1[n//2]

dsu = DSU(N+1)
for a, b in edge:
    if {a,b} == {u,v}:
        continue
    dsu.merge(a,b)

if dsu.size(1) <= dsu.size(N):
    print('Snuke')
else:
    print('Fennec')