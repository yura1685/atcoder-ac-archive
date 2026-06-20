N = input()
M = len(N)
K = int(input())

dp = [[[0, 0] for _ in range(4)] for _ in range(M+1)]
dp[0][0][1] = 1

for i, n in enumerate(N):
    for k in range(4):
        for b in range(2):
            if dp[i][k][b] == 0:
                continue
            if b == 0:
                for m in range(10):
                    if m != 0 and k + 1 <= 3:
                        dp[i+1][k+1][0] += dp[i][k][0]
                    elif m == 0:
                        dp[i+1][k][0] += dp[i][k][0]
            else:
                n = int(n)
                for m in range(n):
                    if m != 0 and k + 1 <= 3:
                        dp[i+1][k+1][0] += dp[i][k][1]
                    elif m == 0:
                        dp[i+1][k][0] += dp[i][k][1]                
                if n != 0 and k + 1 <= 3:
                    dp[i+1][k+1][1] += dp[i][k][1]
                elif n == 0:
                    dp[i+1][k][1] += dp[i][k][1]

print(dp[M][K][0] + dp[M][K][1])