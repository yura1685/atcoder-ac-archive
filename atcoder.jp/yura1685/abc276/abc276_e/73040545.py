from collections import deque

H, W = map(int, input().split())
C = [input() for _ in range(H)]
for h in range(H):
    for w in range(W):
        if C[h][w] == 'S':
            sh, sw = h, w 

cnt = [[0]*W for _ in range(H)]
c = [(-1,0),(0,-1),(0,1),(1,0)]

for h, w in [(sh-1,sw), (sh,sw-1), (sh,sw+1), (sh+1,sw)]:
    if not (0 <= h < H and 0 <= w < W) or C[h][w] == '#':
        continue
    d = deque([(h,w)])
    check = [[0]*W for _ in range(H)]
    check[h][w] = 1
    cnt[h][w] += 1
    while d:
        h, w = d.popleft()
        for dh, dw in c:
            nh, nw = h + dh, w + dw
            if not (0 <= nh < H and 0 <= nw < W):
                continue
            if check[nh][nw] or C[nh][nw] != '.':
                continue
            check[nh][nw] = 1
            cnt[nh][nw] += 1
            d.append((nh,nw))

M = max(max(L) for L in cnt)
print('Yes' if M > 1 else 'No')