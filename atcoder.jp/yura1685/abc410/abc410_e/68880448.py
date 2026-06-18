N, H, M = map(int,input().split())

dp = [[-1]*(M+1) for _ in range(N+1)]
dp[0] = [H] * (M+1)
# dp[i][m] = i 体目を倒したときに魔力が m であるときの体力の最大値

for i in range(1,N+1):
    A, B = map(int,input().split())
    for m in range(M+1):
        if m + B <= M:
            dp[i][m] = max(dp[i-1][m] - A, dp[i-1][m+B])
        else:
            dp[i][m] = dp[i-1][m] - A

for i in range(N+1):
    if max(dp[i]) < 0:
        exit(print(i-1))
print(N)