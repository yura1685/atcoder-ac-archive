N = int(input())
A = list(map(int, input().split()))
dp = [[0] * 1001 for _ in range(6)]
dp[0][0] = 1

for a in A:
    for j in range(5, 0, -1):
        for s in range(1000, a-1, -1):
            dp[j][s] += dp[j-1][s-a]

print(dp[5][1000])