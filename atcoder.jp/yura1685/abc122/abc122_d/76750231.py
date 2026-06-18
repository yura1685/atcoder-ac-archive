N = int(input())

# dp[i文字][最後][最後から2][最後から3] の数
dp = [[[[0] * 5 for _ in range(5)] for _ in range(5)] for _ in range(N+1)]
dp[0][0][0][0] = 1
# A, C, G, T → 1, 2, 3, 4
# アウトなやつ　→　132, 312, 123, 1?32, 13?2
for i in range(N):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                if dp[i][j][k][l] == 0:
                    continue
                for nxt in range(1, 5):
                    if (k, l, nxt) in [(1, 3, 2), (3, 1, 2), (1, 2, 3)]:
                        pass
                    elif (j, l, nxt) == (1, 3, 2):
                        pass
                    elif (j, k, nxt) == (1, 3, 2):
                        pass
                    else:
                        dp[i+1][k][l][nxt] += dp[i][j][k][l]

ans = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            ans += dp[N][i][j][k]
print(ans % 1000000007)