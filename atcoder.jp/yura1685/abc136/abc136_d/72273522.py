S = input()
N = len(S)
dp = [[-1] * 60 for _ in range(N)]
for i in range(N):
    if S[i] == 'L':
        dp[i][0] = i-1
    else:
        dp[i][0] = i+1

for j in range(59):
    for i in range(N):
        dp[i][j+1] = dp[dp[i][j]][j]

ans = [0] * N
for a in list(zip(*dp))[-1]: ans[a] += 1

print(*ans)