from atcoder.maxflow import MFGraph

inf = 10 ** 18
H, W = map(int, input().split())
A = [input() for _ in range(H)]
g = MFGraph(H + W)
for h in range(H):
    for w in range(W):
        if A[h][w] == 'S':
            s = h
            g.add_edge(h, w+H, inf)
            g.add_edge(w+H, h, inf)
        elif A[h][w] == 'T':
            t = w + H
            g.add_edge(h, w+H, inf)
            g.add_edge(w+H, h, inf)
        elif A[h][w] == 'o':
            g.add_edge(h, w+H, 1)
            g.add_edge(w+H, h, 1)

ans = g.flow(s, t)
print(ans if ans < inf else -1)