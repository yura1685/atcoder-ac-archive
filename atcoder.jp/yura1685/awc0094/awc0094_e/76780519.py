from collections import deque

H, W = map(int, input().split())
g = [input() for _ in range(H)]
inf = 10 ** 18
step = [[inf] * W for _ in range(H)]
for h in range(H):
    for w in range(W):
        if g[h][w] == 'S':
            sh, sw = h, w
        if g[h][w] == 'G':
            gh, gw = h, w
step[sh][sw] = 0
dq = deque([(sh, sw)])
while dq:
    h, w = dq.popleft()
    now = g[h][w]
    for dh, dw in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        nh, nw = h + dh, w + dw
        if not (0 <= nh < H and 0 <= nw < W):
            continue
        nxt = g[nh][nw]
        if nxt == 'X':
            continue
        move = 0 if now == nxt == 'V' else 1 if nxt != 'V' else 2
        if step[nh][nw] > step[h][w] + move:
            step[nh][nw] = step[h][w] + move
            if move == 0:
                dq.appendleft((nh, nw))
            else:
                dq.append((nh, nw))

print(step[gh][gw] if step[gh][gw] < inf else 'NO')