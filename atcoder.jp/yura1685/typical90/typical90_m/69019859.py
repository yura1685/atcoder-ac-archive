from sortedcontainers import SortedList

N, M = map(int,input().split())
g = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int,input().split())
    g[A].append((C,B))
    g[B].append((C,A))

inf = float('inf')

go = [inf]*(N+1)
sl = SortedList()
sl.add((0,1))
while sl:
    d, u = sl.pop(0)
    if go[u] < d:
        continue
    go[u] = d
    for w, v in g[u]:
        if go[v] > go[u] + w:
            go[v] = go[u] + w
            sl.add((go[v],v))

back = [inf]*(N+1)
sl = SortedList()
sl.add((0,N))
while sl:
    d, u = sl.pop(0)
    if back[u] < d:
        continue
    back[u] = d
    for w, v in g[u]:
        if back[v] > back[u] + w:
            back[v] = back[u] + w
            sl.add((back[v],v))

for k in range(1,N+1):
    print(go[k]+back[k])