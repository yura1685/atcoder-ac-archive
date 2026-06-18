S = input()
N = len(S)
mod = 10**9 + 7
dp = [[0]*13 for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    s = S[N-i-1]
    if s != '?':
        X = [int(s)*pow(10,i,13)%13]
    else:
        n = pow(10,i,13)
        X = [n*k % 13 for k in range(10)]
    for j in range(13):
        for p in X:
            dp[i+1][(j+p)%13] += dp[i][j]
    for j in range(13):
        dp[i+1][j] %= mod
        
print(dp[N][5] % mod)