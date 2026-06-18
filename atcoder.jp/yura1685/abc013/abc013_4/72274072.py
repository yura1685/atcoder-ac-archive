N, M, D = map(int,input().split())
A = [int(x)-1 for x in input().split()]

Y = [i for i in range(N)]
for a in A:
    Y[a], Y[a+1] = Y[a+1], Y[a]

X = [-1] * N
for i in range(N):
    X[Y[i]] = i

dp = [[-1]*N for _ in range(35)]
for i in range(N):
    dp[0][i] = X[i]

for j in range(34):
    for i in range(N):
        dp[j+1][i] = dp[j][dp[j][i]]

ans = list(range(N))

for b in range(35):
    if D >> b & 1:
        for i in range(N):
            ans[i] = dp[b][ans[i]]
        
for a in ans:
    print(a+1)