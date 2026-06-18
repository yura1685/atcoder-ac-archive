from collections import deque

inf = float('inf')
N, M = map(int,input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
S = input()
ok, ng = [], []
for i in range(N):
    if S[i] == 'S':
        ok.append(i)
    else:
        ng.append(i)

def bfs(L):
    dist = [inf] * N
    dq = deque()
    for l in L:
        dist[l] = 0
        dq.append(l)
    while dq:
        u = dq.popleft()
        for v in g[u]:
            if dist[v] < inf:
                continue
            dist[v] = dist[u] + 1
            dq.append(v)
    return dist

ans = [inf] * len(ng)
for k in range(20):
    L1, L2 = [], []
    for u in ok:
        if (u >> k) & 1:
            L1.append(u)
        else:
            L2.append(u)
    d1, d2 = bfs(L1), bfs(L2)
    for i in range(len(ng)):
        u = ng[i]
        ans[i] = min(ans[i], d1[u] + d2[u])

print(*ans, sep='\n')