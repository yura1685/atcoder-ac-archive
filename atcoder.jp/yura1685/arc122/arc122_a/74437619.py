N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7
dp = [[0, 0] for _ in range(N)]
dp[0][0] = 1
dp2 = [[0, 0] for _ in range(N)]
dp2[0][0] = A[0]
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + dp[i-1][1] % mod
    dp[i][1] = dp[i-1][0]
    dp2[i][0] = (dp2[i-1][0] + dp[i-1][0] * A[i] + 
                 dp2[i-1][1] + dp[i-1][1] * A[i]) % mod
    dp2[i][1] = (dp2[i-1][0] - dp[i-1][0] * A[i]) % mod
print(sum(dp2[N-1]) % mod)