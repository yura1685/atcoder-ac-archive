K = int(input())
if K % 9: exit(print(0))
mod = 10**9 + 7

dp = [0] * (K+1)
dp[0] = 1
for i in range(1, K+1):
    for j in range(1, min(i, 9)+1):
        dp[i] += dp[i-j]
    dp[i] %= mod

print(dp[K])