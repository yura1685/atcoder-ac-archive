N, M = map(int,input().split())
A = list(map(int,input().split()))

dp = [[0]+[-float('inf')]*M for _ in range(N+1)] # dp[i][j]: Ai個まででj個選んだときの最大値

for i in range(1,N+1):
    for j in range(1,M+1):
        if i < j:
            continue
        dp[i][j] = max(dp[i-1][j-1]+j*A[i-1],dp[i-1][j])

print(dp[-1][-1])