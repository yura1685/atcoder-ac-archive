N, M = map(int,input().split())
g = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int,input().split())
    g[A].append((B,C))

inf = float('inf')
dp = [[[inf]*(N+1) for _ in range(N+1)] for _ in range(N+1)]

for s in range(1,N+1):
    for t, w in g[s]:
        dp[s][t][0] = w
    dp[s][s][0] = 0

for k in range(N):
    for s in range(1,N+1):
        for t in range(1,N+1):
            dp[s][t][k+1] = min(dp[s][t][k], dp[s][k+1][k]+dp[k+1][t][k])

ans = 0
for s in range(1,N+1):
    for t in range(1,N+1):
        for k in range(1,N+1):
            if dp[s][t][k] < inf:
                ans += dp[s][t][k] 

print(ans)