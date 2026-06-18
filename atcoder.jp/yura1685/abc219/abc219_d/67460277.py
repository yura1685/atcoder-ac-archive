N = int(input())
X, Y = map(int,input().split())
bento = [tuple(map(int,input().split())) for _ in range(N)]

# dp[i][j][k] = i番目までの弁当で，たこ焼きjたいやきk個買うときの最小値
dp = [[[float('inf')]*(Y+1) for _ in range(X+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
    Tk, Ti = bento[i]
    for j in range(X+1):
        for k in range(Y+1):
            # 弁当を選ばない場合
            dp[i+1][j][k] = min(dp[i+1][j][k],dp[i][j][k])
            # 弁当を選ぶ場合
            nj = min(X, j+Tk)
            nk = min(Y, k+Ti)
            dp[i+1][nj][nk] = min(dp[i+1][nj][nk], dp[i][j][k] + 1)

ans = dp[N][X][Y]

print(ans if ans != float('inf') else -1)