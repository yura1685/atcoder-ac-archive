from collections import deque
H, W = map(int, input().split())
gh, gw = map(int, input().split())
gh, gw = gh-1, gw-1
s = [input() for _ in range(H)]
ans = [[False] * W for _ in range(H)]
ans[gh][gw] = True
dq = deque([(gh, gw)])
dir = [(-1, 0, 'v'), (0, -1, '>'), (0, 1, '<'), (1, 0, '^')]
while dq:
    h, w = dq.popleft()
    for dh, dw, y in dir:
        nh, nw = h + dh, w + dw
        if 0 <= nh < H and 0 <= nw < W and not ans[nh][nw] and (s[nh][nw] == '.' or s[nh][nw] == y):
            dq.append((nh, nw))
            ans[nh][nw] = True
L = [[''] * W for _ in range(H)]
for h in range(H):
    for w in range(W):
        L[h][w] = 'o' if ans[h][w] else '#' if s[h][w] == '#' else 'x'
for l in L:
    print(''.join(l))