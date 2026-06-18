S = ' ' + input()
N = len(S) - 1
mod = 998244353
dp = [[0] * (N+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    s = S[i]
    for j in range(N+1):
        if s != ')':
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % mod
        if s != '(':
            if j < N:
                dp[i][j] = (dp[i][j] + dp[i-1][j+1]) % mod

print(dp[N][0])