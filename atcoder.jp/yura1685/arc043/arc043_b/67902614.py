N = int(input())
mod = 10**9 + 7

d = [int(input()) for _ in range(N)]
DM = max(d)

dp = [[0]*(DM+1) for _ in range(4)]

c = [0]*(DM+1)
for D in d:
    c[D] += 1
    
for i in range(1,DM+1):
    dp[0][i] = (c[i] + dp[0][i-1]) % mod    
    dp[1][i] = (dp[0][i//2]*c[i] + dp[1][i-1]) % mod
    dp[2][i] = (dp[1][i//2]*c[i] + dp[2][i-1]) % mod
    dp[3][i] = (dp[2][i//2]*c[i] + dp[3][i-1]) % mod

print(dp[-1][-1] % mod)