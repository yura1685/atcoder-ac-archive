from collections import deque

H, W = map(int,input().split())
S = [input() for _ in range(H)]
a, b, c, d = map(int,input().split())
a, b, c, d = a-1, b-1, c-1, d-1
D = [(-1,0),(0,-1),(0,1),(1,0)]

step = [[10**8]*W for _ in range(H)]
step[a][b] = 0

dq = deque([(a,b,0)])
while dq:
    h, w, s = dq.popleft()
    if s > step[h][w]:
        continue
    for dh, dw in D:
        nh, nw = h+dh, w+dw
        if not (0 <= nh < H and 0 <= nw < W):
            continue
        if step[nh][nw] > step[h][w] + (S[nh][nw] == '#'):
            if S[nh][nw] == '#':
                step[nh][nw] = step[h][w] + 1
                dq.append((nh,nw,step[nh][nw]))
            else:
                step[nh][nw] = step[h][w]
                dq.appendleft((nh,nw,step[nh][nw]))
        nh, nw = nh+dh, nw+dw
        if not (0 <= nh < H and 0 <= nw < W):
            continue
        if step[nh][nw] > step[h][w] + (S[nh][nw] == '#' or S[nh-dh][nw-dw] == '#'):
            if S[nh][nw] == '#' or S[nh-dh][nw-dw] == '#':
                step[nh][nw] = step[h][w] + 1
                dq.append((nh,nw,step[nh][nw]))
            else:
                step[nh][nw] = step[h][w]
                dq.appendleft((nh,nw,step[nh][nw]))

print(step[c][d])