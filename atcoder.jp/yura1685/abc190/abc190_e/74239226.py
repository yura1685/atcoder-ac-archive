from collections import deque

N, M = map(int, input().split())
inf = 10 ** 12
g = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    g[A].append(B)
    g[B].append(A)

K = int(input())
C = list(map(int, input().split()))

def bfs(u):
    dist = [inf] * (N+1)
    dist[u] = 0
    dq = deque([u])
    while dq:
        u = dq.popleft()
        for v in g[u]:
            if dist[v] < inf:
                continue
            dist[v] = dist[u] + 1
            dq.append(v)
    return [dist[c] if dist[c] < inf else -1 for c in C]

D = [bfs(c) for c in C]

for d in D:
    if -1 in d: exit(print(-1))

dp = [[inf] * K for _ in range(1 << K)]
for i in range(K): dp[1 << i][i] = 0

for bit in range(1, 1 << K):
    for x in range(K):
        if dp[bit][x] == inf:
            continue
        for k in range(K):
            if not (bit >> k & 1):
                nex = bit | (1 << k) 
                dp[nex][k] = min(dp[nex][k], dp[bit][x] + D[x][k])

print(min(dp[-1]) + 1)