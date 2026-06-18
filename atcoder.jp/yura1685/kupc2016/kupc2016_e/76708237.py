from atcoder.maxflow import MFGraph

H, W = map(int, input().split())
S = [input() for _ in range(H)]
N = H * W + 2
inf = 10 ** 18
yagi, soto = H * W, H * W + 1
g = MFGraph(2*N)
g.add_edge(yagi, yagi + N, inf)
g.add_edge(soto, soto + N, inf)
for h in range(H):
    for w in range(W):
        up = h * W + w
        do = up + N
        if S[h][w] == '.':
            g.add_edge(up, do, 1)
        else:
            g.add_edge(up, do, inf)
            g.add_edge(do, yagi, inf)
            g.add_edge(yagi + N, up, inf)
        if h == 0 or h == H-1 or w == 0 or w == W-1:
            g.add_edge(do, soto, inf)
            g.add_edge(soto + N, up, inf)
        for dh, dw in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nh, nw = h + dh, w + dw
            if not (0 <= nh < H and 0 <= nw < W):
                continue
            up2 = nh * W + nw
            g.add_edge(do, up2, inf)

ans = g.flow(yagi, soto + N)
print(ans if ans < inf else -1)