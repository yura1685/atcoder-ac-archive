N = int(input())
L = list(map(int,input().split()))

dp = [[0]*(N-1) for _ in range(21)]
dp[L[0]][0] = 1

for i in range(1,N-1):
    num = L[i]
    for n in range(21):
        if dp[n][i-1] == 0:
            continue
        if 0 <= n + num <= 20:
            dp[n+num][i] += dp[n][i-1]
        if 0 <= n - num <= 20:
            dp[n-num][i] += dp[n][i-1]

print(dp[L[-1]][-1])