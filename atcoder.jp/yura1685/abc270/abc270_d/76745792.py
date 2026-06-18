N, K = map(int, input().split())
A = list(map(int, input().split()))
dp = [0] * (N+1)
for i in range(1, N+1):
    M = 0
    for a in A:
        if i < a: break
        M = max(M, a + (i - a) - dp[i-a])
    dp[i] = M
print(dp[N])