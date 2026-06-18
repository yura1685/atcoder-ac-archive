S = input()
N = len(S)
mod = 10**9 + 7

dp = [[0]*(N+1) for _ in range(9)]
dp[0][0] = 1

for j in range(N):
    s = S[j]
    for i in range(9):
        dp[i][j+1] = dp[i][j]

    if s == 'c': dp[1][j+1] = (dp[0][j] + dp[1][j]) % mod
    if s == 'h': dp[2][j+1] = (dp[1][j] + dp[2][j]) % mod
    if s == 'o': dp[3][j+1] = (dp[2][j] + dp[3][j]) % mod
    if s == 'k': dp[4][j+1] = (dp[3][j] + dp[4][j]) % mod
    if s == 'u': dp[5][j+1] = (dp[4][j] + dp[5][j]) % mod
    if s == 'd': dp[6][j+1] = (dp[5][j] + dp[6][j]) % mod
    if s == 'a': dp[7][j+1] = (dp[6][j] + dp[7][j]) % mod
    if s == 'i': dp[8][j+1] = (dp[7][j] + dp[8][j]) % mod

print(dp[-1][-1])