N, M = map(int,input().split())
S = [0] + list(map(int,input().split()))
T = [0] + list(map(int,input().split()))
mod = 10**9 + 7
dp = [[0] * (M+1) for _ in range(N+1)]
AC = [[0] * (M+1) for _ in range(N+1)]


for i in range(1,N+1):
    for j in range(1,M+1):
        if S[i] != T[j]:
            dp[i][j] = 0
        else:
            dp[i][j] = AC[i-1][j-1] + 1
        AC[i][j] = (AC[i][j-1] + AC[i-1][j] - AC[i-1][j-1] + dp[i][j]) % mod

print((AC[-1][-1] + 1) % mod)