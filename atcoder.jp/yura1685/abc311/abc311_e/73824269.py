H, W, N = map(int,input().split())
G = [['.'] * W for _ in range(H)]
for _ in range(N):
    a, b = map(int, input().split())
    G[a-1][b-1] = '#'
dp = [[0] * W for _ in range(H)]

for h in range(H):
    dp[h][-1] = 0 if G[h][-1] == '#' else 1
for w in range(W):
    dp[-1][w] = 0 if G[-1][w] == '#' else 1

for h in range(H-2, -1, -1):
    for w in range(W-2, -1, -1):
        if G[h][w] == '#':
            dp[h][w] = 0
        else:
            dp[h][w] = min(dp[h+1][w], dp[h][w+1], dp[h+1][w+1]) + 1

print(sum(sum(l) for l in dp))