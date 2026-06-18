N, ma, mb = map(int,input().split())
inf = float('inf')
dp = [[[inf]*500 for _ in range(500)] for _ in range(N+1)]
dp[0][0][0] = 0

for n in range(N):
    a, b, c = map(int,input().split())
    for i in range(401):
        for j in range(401):
            dp[n+1][i][j] = min(dp[n+1][i][j], dp[n][i][j])
            dp[n+1][i+a][j+b] = min(dp[n][i+a][j+b], dp[n][i][j]+c)

ans = inf
for i in range(1,401):
    for j in range(1,401):
        if i * mb == j * ma:
            ans = min(ans, dp[N][i][j])

print(ans if ans < inf else -1)