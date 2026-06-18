H, W, K = map(int, input().split())
sh, sw = map(int, input().split())
sh, sw = sh-1, sw-1
A = [list(map(int, input().split())) for _ in range(H)]
inf = 10 ** 18
dp = [[[-inf] * W for _ in range(H)] for _ in range(H*W)]

dp[0][sh][sw] = 0
dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]
for step in range(H*W-1):
    for h in range(H):
        for w in range(W):
            if dp[step][h][w] < 0:
                continue
            for dh, dw in dir:
                nh, nw = h + dh, w + dw
                if not (0 <= nh < H and 0 <= nw < W): continue
                dp[step+1][nh][nw] = max(dp[step+1][nh][nw],
                                         dp[step][h][w] + A[nh][nw])

ans = 0
for step in range(H*W):
    if step > K: break
    for h in range(H):
        for w in range(W):
            if dp[step][h][w] < 0:
                continue
            ans = max(ans, dp[step][h][w] + (K - step) * A[h][w])
print(ans)