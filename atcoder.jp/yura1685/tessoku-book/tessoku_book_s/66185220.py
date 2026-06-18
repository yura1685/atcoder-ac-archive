N, W = map(int,input().split())

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(1,N+1):
    wi, vi = map(int,input().split())
    for w in range(W+1):
        if w - wi < 0:
            dp[i][w] = dp[i-1][w]
        else:
            x = dp[i-1][w-wi] + vi #入れるパターン
            y = dp[i-1][w] #入れないパターン
            dp[i][w] = max(x,y)

print(dp[N][W])