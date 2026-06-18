N, M = map(int,input().split())
X = N+M+1
P = [(0,0)] + [tuple(map(int,input().split())) for _ in range(N+M)]
dist = [[0]*(X) for _ in range(X)]

for i in range(X):
    for j in range(X):
        dist[i][j] = ((P[i][0] - P[j][0]) ** 2 + (P[i][1] - P[j][1]) ** 2) ** (1/2)

inf = float('inf')
dp = [[inf] * X for _ in range(1 << X)]
dp[1][0] = 0

for mask in range(1 << X):
    for u in range(X):
        if dp[mask][u] == inf:
            continue
        for v in range(X):
            if (mask >> v) & 1:
                continue
            new_mask = mask | (1 << v)
            cnt = (mask >> (N+1)).bit_count()
            dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v]*0.5**cnt)

ans = inf
for mask in range(1 << X):
    if mask & ((1 << N+1) - 1) == (1 << N+1) - 1:
        cnt = (mask >> (N+1)).bit_count()
        for u in range(X):
            ans = min(ans, dp[mask][u] + dist[u][0]*0.5**cnt)

print(ans)