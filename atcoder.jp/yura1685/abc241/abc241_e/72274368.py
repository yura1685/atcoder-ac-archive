N, K = map(int,input().split())
A = list(map(int,input().split()))

dp1 = [[-1]*N for _ in range(45)]
# dp[j][i]: i番目皿の2^j回後の皿
for i in range(N):
    dp1[0][i] = (i + A[i]) % N
for j in range(44):
    for i in range(N):
        dp1[j+1][i] = dp1[j][dp1[j][i]]

dp2 = [[-1]*N for _ in range(45)]
# dp2[j][i]: i番目の皿を含めて、2^j回で乗っける飴の個数
# dp2[j+1][i]: dp2[j][i] + dp2[j][dp1[j][i]]
for i in range(N):
    dp2[0][i] = A[i]
for j in range(44):
    for i in range(N):
        dp2[j+1][i] = dp2[j][i] + dp2[j][dp1[j][i]]

now = 0
ans = 0
for j in range(45):
    if K >> j & 1:
        ans += dp2[j][now]
        now  = dp1[j][now]

print(ans)