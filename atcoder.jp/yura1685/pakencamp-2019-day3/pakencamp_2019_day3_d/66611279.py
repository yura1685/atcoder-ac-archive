N = int(input())
S = [input() for _ in range(5)]
S = list(zip(*S))

dp = [[0]+[10**5]*N for _ in range(3) ]

for i in range(N):
    z = S[i]
    R, B, W = 5-z.count('R'), 5-z.count('B'), 5-z.count('W')
    dp[0][i+1] = min(dp[1][i],dp[2][i]) + R
    dp[1][i+1] = min(dp[0][i],dp[2][i]) + B
    dp[2][i+1] = min(dp[0][i],dp[1][i]) + W

print(min([dp[i][-1] for i in range(3)]))