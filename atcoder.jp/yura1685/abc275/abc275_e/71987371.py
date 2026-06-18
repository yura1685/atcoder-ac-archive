N, M, K = map(int,input().split())

dp = [[0] * (N+1) for _ in range(K+1)]
dp[0][0] = 1
mod = 998244353
inv = pow(M, mod-2, mod)

for i in range(K):
    for j in range(N):
        for m in range(1,M+1):
            nex = j + m
            if nex > N: nex = N - (nex-N)
            dp[i+1][nex] += dp[i][j] * inv
            dp[i+1][nex] %= mod
    dp[i+1][N] += dp[i][N]
    dp[i+1][N] %= mod

print(dp[K][N])