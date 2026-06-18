from collections import deque

dir = [(-1,0), (0,-1), (0,1), (1,0)]
H, W = map(int, input().split())
inf = 10 ** 8
S = [input() for _ in range(H)]
C = [[inf] * W for _ in range(H)]
C[0][0] = 0

d = deque([(0, 0)])
while d:
    h, w = d.popleft()
    for dh, dw in dir:
        nh, nw = h + dh, w + dw
        if not (0 <= nh < H and 0 <= nw < W):
            continue
        if C[nh][nw] > C[h][w] + 1 and S[h][w] != S[nh][nw]:
            C[nh][nw] = C[h][w] + 1
            d.append((nh, nw))

print(C[-1][-1] if C[-1][-1] < inf else -1)