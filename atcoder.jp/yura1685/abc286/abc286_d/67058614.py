N, X = map(int,input().split())

dp = [[False]*(X+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(1,N+1):
    A, B = map(int,input().split())
    for j in range(X+1):
        for k in range(B+1):
            if j - A*k < 0:
                break
            if dp[i-1][j-A*k]:
                dp[i][j] = True

print('Yes' if dp[-1][-1] else 'No')