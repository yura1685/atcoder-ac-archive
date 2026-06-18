N, M, K = map(int,input().split())
mod = 998244353

dp = [[0]*(K+1) for _ in range(N+1)]
# dp[i][j]: 項数iまでで総和がjとなる総数
dp[0][0] = 1
for i in range(1,N+1):
    for j in range(1,K+1):
        for k in range(1,M+1):
            if j-k < 0:
                continue
            dp[i][j] += dp[i-1][j-k]
        dp[i][j] %= mod

print(sum(dp[-1]) % mod)