K = input()
N = len(K)
D = int(input())
mod = 10 ** 9 + 7
dp = [[[0] * 2 for _ in range(D)] for _ in range(N+1)]
dp[0][0][1] = 1
for i, n in enumerate(K):
    for j in range(D):
        for k in range(2):
            if dp[i][j][k] == 0:
                continue
            if k == 0:
                for nxt in range(10):
                    dp[i+1][(j+nxt)%D][0] += dp[i][j][k]
                    dp[i+1][(j+nxt)%D][0] %= mod
            else:
                for nxt in range(int(n)):
                    dp[i+1][(j+nxt)%D][0] += dp[i][j][k]
                    dp[i+1][(j+nxt)%D][0] %= mod
                dp[i+1][(j+int(n))%D][1] += dp[i][j][k]
                dp[i+1][(j+int(n))%D][1] %= mod

print((sum(dp[N][0]) - 1) % mod)