N, M = map(int,input().split())
Keys = []
for _ in range(M):
    a, b = map(int,input().split())
    c = list(map(int, input().split()))
    tre = 0
    for bit in c:
        tre |= 1 << (bit - 1)
    Keys.append((a, tre))

inf = 10 ** 9

dp = [[inf] * (1 << N) for _ in range(M+1)]
dp[0][0] = 0
for i in range(M):
    a, c = Keys[i]
    for j in range(1 << N):
        j2 = j | c
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        dp[i+1][j2] = min(dp[i+1][j2], dp[i][j] + a)
        

print(dp[-1][-1] if dp[-1][-1] < 10**9 else -1)