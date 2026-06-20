N, K = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * 40
for i in range(40):
    cnt = 0
    for a in A:
        if (a >> i) & 1:
            cnt += 1
    B[39-i] = cnt
K = bin(K)[2:].zfill(40)
dp = [[-1, -1] for _ in range(41)]
dp[0][1] = 0

for i, k in enumerate(K):
    for b in range(2):
        if dp[i][b] == -1:
            continue
        if b == 0:
            dp[i+1][b] = max(dp[i+1][b], dp[i][b] + max(B[i], N - B[i]) * pow(2, 40-i-1))
        else:
            if k == '0':
                dp[i+1][1] = max(dp[i+1][1], dp[i][1] + B[i] * pow(2, 40-i-1))
            else:
                dp[i+1][0] = max(dp[i+1][0], dp[i][1] + B[i] * pow(2, 40-i-1))
                dp[i+1][1] = max(dp[i+1][1], dp[i][1] + (N - B[i]) * pow(2, 40-i-1))

print(max(dp[40]))