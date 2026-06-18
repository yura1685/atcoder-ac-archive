from collections import deque

c1 = [(-1,0),(0,-1),(0,1),(1,0)]
c2 = [(-2,-1),(-2,0),(-2,1),(-1,-2),(-1,-1),(-1,0),(-1,1),(-1,2),(0,-2),(0,-1),
     (0,1),(0,2),(1,-2),(1,-1),(1,0),(1,1),(1,2),(2,-1),(2,0),(2,1)]

H, W = map(int,input().split())
S = [input() for _ in range(H)]
P = [[16851685]*W for _ in range(H)]
P[0][0] = 0
d = deque([(0,0)])
while d:
    h, w = d.popleft()
    for dh, dw in c1:
        nh, nw = h+dh, w+dw
        if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and P[h][w] < P[nh][nw]:
            P[nh][nw] = P[h][w]
            d.appendleft((nh,nw))
    for dh, dw in c2:
        nh, nw = h+dh, w+dw
        if 0 <= nh < H and 0 <= nw < W and P[h][w] + 1 < P[nh][nw]:
            P[nh][nw] = P[h][w] + 1
            d.append((nh,nw))

print(P[-1][-1])