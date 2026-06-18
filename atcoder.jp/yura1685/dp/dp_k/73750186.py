N, K = map(int,input().split())
A = list(map(int,input().split()))
dp = [[None] * (K + 1) for _ in range(2)]
# dp[i][j]: iのターンで石がj個のときの勝者
# i=0 -> 後手 i=1 -> 先手　False -> 後手 True -> 先手

dp[0][0] = True
dp[1][0] = False

for j in range(1, K+1):
    for a in A:
        if j - a < 0:
            break
        if dp[0][j-a] == True:
            dp[1][j] = True
            break
    if dp[1][j] == None:
        dp[1][j] = False
    
    for a in A:
        if j - a < 0:
            break
        if dp[1][j-a] == False:
            dp[0][j] = False
            break
    if dp[0][j] == None:
        dp[0][j] = True

ans = dp[1][K]
print('First' if ans else 'Second')