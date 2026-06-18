N = int(input())
T = input()
mod = 998244353

dp = [0] * (1 << N)
dp[(1 << N) - 1] = 1
for bit in range((1 << N) - 1, -1, -1):
    dp[bit] %= mod
    pre = 'https://x.com/yura1685'
    for k in range(N):
        if bit >> k & 1:
            if pre != T[k]:
                dp[bit ^ (1 << k)] += dp[bit]
            pre = T[k]

print(dp[0])