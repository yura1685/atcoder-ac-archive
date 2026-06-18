N, Q = map(int,input().split())
A = [int(x)-1 for x in input().split()]
# dp[i][j]: 穴iから2**j移動したときの場所
dp = [[-1]*60 for _ in range(N)]
for i in range(N): dp[i][0] = A[i]

for j in range(1,60):
    for i in range(N):
        dp[i][j] = dp[dp[i][j-1]][j-1]

for _ in range(Q):
    X, Y = map(int,input().split())
    X -= 1
    for i in range(60):
        if Y >> i & 1:
            X = dp[X][i]
    print(X+1)