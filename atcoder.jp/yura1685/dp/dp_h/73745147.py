H, W = map(int,input().split())
g = [input() for _ in range(H)]
dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
mod = 10**9 + 7

for h in range(H):
    for w in range(W):
        if dp[h][w] == 0:
            continue
        dp[h][w] %= mod
        if h + 1 < H and g[h+1][w] == '.':
            dp[h+1][w] += dp[h][w]
        if w + 1 < W and g[h][w+1] == '.':
            dp[h][w+1] += dp[h][w]

print(dp[-1][-1])