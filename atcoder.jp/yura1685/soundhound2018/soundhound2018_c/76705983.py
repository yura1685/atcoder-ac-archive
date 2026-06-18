from atcoder.maxflow import MFGraph

H, W = map(int, input().split())
N = H * W
S = [input() for _ in range(H)]
g = MFGraph(N + 2)
cnt = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == '*':
            continue
        cnt += 1
        if (h + w) % 2 == 0:
            g.add_edge(N, h*W + w, 1)
        else:
            g.add_edge(h*W + w, N+1, 1)
        if h + 1 < H and S[h+1][w] == '.':
            a, b = h*W+w, (h+1)*W+w
            if (h + w) % 2 == 0:
                g.add_edge(a, b, 1)
            else:
                g.add_edge(b, a, 1)
        if w + 1 < W and S[h][w+1] == '.':
            a, b = h*W+w, h*W+w+1
            if (h + w) % 2 == 0:
                g.add_edge(a, b, 1)
            else:
                g.add_edge(b, a, 1)

print(cnt - g.flow(N, N+1))