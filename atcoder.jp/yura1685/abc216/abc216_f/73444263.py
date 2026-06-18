N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
Q = sorted((a, b) for a, b in zip(A,B))
M = max(A)
mod = 998244353
dp = [[0] * (M+1) for _ in range(N+1)]
dp[0][0] = 1
ans = 0

for i in range(N):
    a, b = Q[i]
    for j in range(M+1):
        dp[i+1][j] = dp[i][j]
        if Q[i][1] <= j:
            dp[i+1][j] += dp[i][j-Q[i][1]]
            dp[i+1][j] %= mod
        if j <= Q[i][0] - Q[i][1]:
            ans += dp[i][j]
            ans %= mod

print(ans)