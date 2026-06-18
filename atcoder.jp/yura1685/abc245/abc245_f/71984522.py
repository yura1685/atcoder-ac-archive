from atcoder.scc import SCCGraph
from collections import deque

N, M = map(int,input().split())
G = SCCGraph(N)
rg = [[] for _ in range(N)]
for _ in range(M):
    U, V = map(int,input().split())
    U, V = U-1, V-1
    G.add_edge(U, V)
    rg[V].append(U)

can = [False] * N
scc = G.scc()
dq = deque()

for g in scc:
    if len(g) > 1:
        for u in g:
            can[u] = True
            dq.append(u)

while dq:
    u = dq.popleft()
    for v in rg[u]:
        if can[v]: continue
        dq.append(v)
        can[v] = True

print(sum(can))