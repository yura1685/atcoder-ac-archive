N, X = map(int, input().split())
T = list(map(int, input().split()))

mod = 998244353
p = pow(N, -1, mod)
dp = [p] + [0] * X
for i in range(1, X+1):
    q = 0
    for t in T:
        if i - t >= 0:
            q += dp[i-t]
    dp[i] = p * q % mod

print(sum(dp[X-T[0]+1:X+1]) % mod)