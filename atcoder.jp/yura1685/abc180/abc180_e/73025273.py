N = int(input())

cities = []
for _ in range(N):
    X, Y, Z = map(int,input().split())
    cities.append((X,Y,Z))

dist = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        xi, yi, zi = cities[i]
        xj, yj, zj = cities[j]
        dist[i][j] = abs(xi-xj) + abs(yi-yj) + max(0,zj-zi)

inf = float('inf')
dp = [[inf]*N for _ in range(1<<N)]
dp[1][0] = 0

for mask in range(1, 1 << N):
    for u in range(N):
        if dp[mask][u] == inf:
            continue
        for v in range(N):
            if ((mask >> v) & 1):
                continue
            new_mask = mask | (1 << v)
            if dp[mask][u] + dist[u][v] < dp[new_mask][v]:
                dp[new_mask][v] = dp[mask][u] + dist[u][v]

ans = inf
for i in range(1,N):
    ans = min(ans, dp[-1][i] + dist[i][0])

print(ans)