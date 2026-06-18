N = int(input())
P = list(map(float, input().split()))

# dp[i][j] = i 枚目までのコインを投げて，表が j 枚のときの確率
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    p = P[i]
    for j in range(i+2):
        if j == 0:
            dp[i+1][0] = (1 - p) * dp[i][0]
            continue
        dp[i+1][j] = p * dp[i][j-1] + (1 - p) * dp[i][j]

ans = 0
for j in range((N+1)//2,N+1):
    ans += dp[N][j]

print(ans)