H, W = map(int,input().split())
S = [input() for _ in range(H)]
d = {'+':1, '-':-1}
dp = [[0]*W for _ in range(H)]

for i in range(H-1,-1,-1):
    for j in range(W-1,-1,-1):
        if (i, j) == (H-1, W-1):
            continue
        elif i == H-1:
            dp[i][j] = dp[i][j+1] + (d[S[i][j+1]] if (i+j) % 2 == 0 else -d[S[i][j+1]])
        elif j == W-1:
            dp[i][j] = dp[i+1][j] + (d[S[i+1][j]] if (i+j) % 2 == 0 else -d[S[i+1][j]])
        elif (i + j) % 2 == 0:
            dp[i][j] = max(dp[i+1][j] + d[S[i+1][j]], dp[i][j+1] + d[S[i][j+1]])
        else:
            dp[i][j] = min(dp[i+1][j] - d[S[i+1][j]], dp[i][j+1] - d[S[i][j+1]])

ans = dp[0][0]

if abs(ans): ans //= abs(ans)
print(['Draw', 'Takahashi','Aoki'][ans])