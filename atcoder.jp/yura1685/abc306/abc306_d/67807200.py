N = int(input())

dp = [[-float('inf')]*(N+1) for _ in range(2)]
dp[0][0] = 0

for i in range(N):
    X, Y = map(int,input().split())
    if X == 0:
        dp[0][i+1] = max(dp[0][i]+Y,dp[1][i]+Y,dp[0][i])
        dp[1][i+1] = dp[1][i]
    else:
        dp[1][i+1] = max(dp[0][i]+Y,dp[1][i])
        dp[0][i+1] = dp[0][i]

print(max(dp[0][-1],dp[1][-1]))