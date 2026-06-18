N = int(input())
p = list(map(int,input().split()))

dp = [[0]*(sum(p)+1) for _ in range(N+1)]

dp[0][0] = 1

for i in range(N):
    x = p[i]
    for j in range(sum(p)+1):
        if dp[i][j] == 1:
            dp[i+1][j] = 1
        if j-x >= 0 and dp[i][j-x] == 1:
            dp[i+1][j] = 1

print(sum(dp[-1]))