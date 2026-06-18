N, M = map(int,input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]

dp = [[10**10]*M for _ in range(N)]

for w in range(M-N+1):
    dp[0][w] = D[0]*C[w]

for h in range(1,N):
    m = 10**10
    for w in range(h,M-N+1+h):
        m = min(m,dp[h-1][w-1])
        dp[h][w] = D[h]*C[w] + m 

print(min(dp[-1]))