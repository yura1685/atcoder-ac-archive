N, A, B, P, Q = map(int,input().split())
mod = 998244353
invP, invQ = pow(P,-1,mod), pow(Q,-1,mod)
dp = [[[0,0] for _ in range(N+1)] for _ in range(N+1)]

for i in range(N,A-1,-1):
    for j in range(N,B-1,-1):
        if i == N:
            dp[i][j] = [1,1]
        elif j == N:
            dp[i][j] = [0,0]
        else:
            for k in range(1,P+1):
                dp[i][j][0] += dp[min(i+k,N)][j][1]
            dp[i][j][0] = dp[i][j][0] * invP % mod
            
            for k in range(1,Q+1):
                dp[i][j][1] += dp[i][min(j+k,N)][0]
            dp[i][j][1] = dp[i][j][1] * invQ % mod

print(dp[A][B][0])