N, M, K = map(int,input().split())

prof = [0] * N
cost = [0] * N
for i in range(N):
    a, b = map(int,input().split())
    prof[i] = a
    cost[i] = b

dp = [[0] * (M+1) for _ in range(N)]
dp[0][cost[0]] = prof[0]

for i in range(1,N):
    dp[i][cost[i]] = max(dp[i][cost[i]], prof[i])
    for j in range(M+1):
        if j < cost[i]:
            continue
        for p in range(max(0,i-K), i):
            if dp[p][j - cost[i]] > 0:
                dp[i][j] = max(dp[i][j], dp[p][j-cost[i]] + prof[i])

print(max(max(L) for L in dp))