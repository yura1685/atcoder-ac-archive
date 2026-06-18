N, S = map(int,input().split())
A = [int(x) for x in input().split()]

dp = [[False]*(S+1) for _ in range(N+1)]
# dp[i][j]: Aiまでで和をSにすることは可能か？

dp[0][0] = True

for i in range(1,N+1):
    a = A[i-1]
    for j in range(S+1):
        if not dp[i-1][j]:
            continue
        dp[i][j] = True
        if j + a <= S:
            dp[i][j+a] = True

print('Yes' if dp[-1][-1] else 'No')