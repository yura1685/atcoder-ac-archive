MOD = 998244353
def solve(N):
    dp = [[0]*6 for _ in range(N+1)]
    for a in range(1, 6):
        dp[1][a] = 1
    for n in range(2, N+1):
        dp[n][1] = (dp[n-1][1] + dp[n-1][2]) % MOD
        dp[n][2] = (dp[n-1][1] + dp[n-1][2] + dp[n-1][3]) % MOD
        dp[n][3] = (dp[n-1][2] + dp[n-1][3] + dp[n-1][4]) % MOD
        dp[n][4] = (dp[n-1][3] + dp[n-1][4] + dp[n-1][5]) % MOD
        dp[n][5] = (2 * dp[n-1][4] + dp[n-1][5]) % MOD
    return dp[N]

N = int(input())
x = solve(N)
print((2*sum(x)-x[-1]) % MOD)