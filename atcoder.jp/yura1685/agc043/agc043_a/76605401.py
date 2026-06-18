from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]
inf = 10 ** 18
step = [[inf] * W for _ in range(H)]
step[0][0] = int(S[0][0] == '#')
dq = deque([(0, 0)])
dir = [(0, 1), (1, 0)]
while dq:
    h, w = dq.popleft()
    for dh, dw in dir:
        nh, nw = h + dh, w + dw
        if not (0 <= nh < H and 0 <= nw < W):
            continue
        b = (S[h][w] == '.' and S[nh][nw] == '#')
        if step[nh][nw] > step[h][w] + int(b):
            step[nh][nw] = step[h][w] + int(b)
            if b:
                dq.append((nh, nw))
            else:
                dq.appendleft((nh, nw))

print(step[H-1][W-1])