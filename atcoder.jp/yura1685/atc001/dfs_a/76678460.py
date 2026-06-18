I = input().split()
H, W = int(I[0]), int(I[1])
S = [input() for _ in range(H)]
sh, sw, gh, gw = -1, -1, -1, -1
for h in range(H):
    for w in range(W):
        if S[h][w] == 's':
            sh, sw = h, w
        if S[h][w] == 'g':
            gh, gw = h, w

visit = [[False] * W for _ in range(H)]
visit[sh][sw] = True

def dfs(h, w):
    for dh, dw in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        nh, nw = h + dh, w + dw
        if not (0 <= nh < H and 0 <= nw < W):
            continue
        if S[nh][nw] == '#':
            continue
        if visit[nh][nw]:
            continue
        visit[nh][nw] = True
        dfs(nh, nw)

dfs(sh, sw)
print('Yes' if visit[gh][gw] else 'No')