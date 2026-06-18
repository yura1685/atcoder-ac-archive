from itertools import accumulate

N = int(input())
P = [0] + list(map(int,input().split()))
pow = [1.0]
for _ in range(N):
    pow.append(pow[-1]*0.9)
spow = list(accumulate(pow))  
dp = [[0.0]*(i+1) for i in range(N+1)]
dp[1][1] = P[1]

for i in range(2,N+1):
    for j in range(1,i+1):
        dp[i][j] = max(dp[i][j], pow[1]*dp[i-1][j-1] + P[i])
        if j <= i-1:
            dp[i][j] = max(dp[i][j], dp[i-1][j])

ans = -10**18
for k in range(1,N+1):
    b = spow[k-1]
    c = 1200 / (k**(1/2))
    ans = max(ans, (dp[-1][k] / b) - c)

print(ans)