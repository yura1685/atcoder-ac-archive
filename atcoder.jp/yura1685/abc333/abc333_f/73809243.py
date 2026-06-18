N = int(input())
mod = 998244353
inv2 = pow(2,-1,mod)
pow2 = [1]
for i in range(N):
    pow2.append(pow2[-1]*2%mod)

dp = [[0] * i for i in range(N+1)]
dp[1][0] = 1

for i in range(2,N+1):
    s = 0
    for j in range(i-1):
        s += pow2[j] * dp[i-1][j]
    s %= mod
    dp[i][0] = s * pow(pow2[i]-1, -1, mod) % mod
    for j in range(1,i):
        dp[i][j] = (dp[i-1][j-1] + dp[i][j-1]) * inv2 % mod

print(*dp[-1])