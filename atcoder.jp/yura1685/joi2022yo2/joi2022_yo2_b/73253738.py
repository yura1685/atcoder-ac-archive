from collections import deque

H, W = map(int,input().split())
S = [input() for _ in range(H)]
c = [(-1,0),(0,-1),(0,1),(1,0)]
inf = H*W+1
step = [[inf]*W for _ in range(H)]
step[0][0] = 0
dq = deque([(0,0)])

while dq:
    h, w = dq.popleft()
    for dh, dw in c:
        nh, nw = h+dh, w+dw
        if not (0 <= nh < H and 0 <= nw < W):
            continue
        if step[h][w] + 1 >= step[nh][nw]:
            continue
        if S[h][w] == S[nh][nw]:
            continue
        step[nh][nw] = step[h][w] + 1
        dq.append((nh,nw))

ans = step[-1][-1]
print(ans if ans < inf else -1)