N, M = map(int,input().split())

g = [[float('INF')]*N for _ in range(N)]
for _ in range(M):
    s, t, d = map(int,input().split())
    g[s-1][t-1] = d
    g[t-1][s-1] = d
for i in range(N):
    g[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            g[i][j] = min(g[i][j], g[i][k]+g[k][j])

ans = float('INF')
for i in range(N):
    ans = min(ans,max(g[i]))

print(ans)