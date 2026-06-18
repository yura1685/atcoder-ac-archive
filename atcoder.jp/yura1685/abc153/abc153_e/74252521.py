H, N = map(int, input().split())
M = 0
AB = []
for _ in range(N):
    A, B = map(int, input().split())
    AB.append((A, B))
    M = max(M, A)

inf = 10 ** 9
dp = [0] + [inf] * (H + M)

for i in range(H+1):
    if dp[i] == inf:
        continue
    for a, b in AB:
        dp[i+a] = min(dp[i+a], dp[i] + b)

print(min(dp[H:]))