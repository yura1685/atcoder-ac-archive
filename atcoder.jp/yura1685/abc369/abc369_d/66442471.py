N = int(input())
A = list(map(int,input().split()))

dp = [[0]*(N+1) for _ in range(2)]
dp[1][0] = -10**18

for i in range(N):
    a = A[i]
    dp[0][i+1] = max(dp[0][i],dp[1][i]+2*a)
    dp[1][i+1] = max(dp[0][i]+a,dp[1][i])

print(max(dp[0][-1],dp[1][-1]))