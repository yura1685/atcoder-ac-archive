from collections import deque

H, W = map(int,input().split())
def sex(n): return int(n)-1
h , w  = map(sex,input().split())
gh, gw = map(sex,input().split())

S = [input() for _ in range(H)]
inf = 10**8
step = [[inf] * W for _ in range(H)]
step[h][w] = 0

move = [(-1,0),(0,-1),(0,1),(1,0)]
warp = []
for dh in range(-2,3):
    for dw in range(-2,3):
        warp.append((dh, dw))

d = deque()
d.append((h,w))

while d:
    h, w = d.popleft()
    for dh, dw in move:
        nh, nw = h + dh, w + dw
        if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and step[h][w] < step[nh][nw]:
            step[nh][nw] = step[h][w]
            d.appendleft((nh,nw))
    for dh, dw in warp:
        nh, nw = h + dh, w + dw
        if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and step[h][w] + 1 < step[nh][nw]:
            step[nh][nw] = step[h][w] + 1
            d.append((nh, nw))

ans = step[gh][gw]
print(ans if ans < inf else -1)