from collections import deque

H, W, D = map(int,input().split())
glid = [list('#' + input() + '#') for _ in range(H)]
glid = [['#']*(W+2)] + glid + [['#']*(W+2)]

d = deque()
for h in range(1,H+1):
    for w in range(1,W+1):
        if glid[h][w] == 'H':
            d.append((h,w))
            glid[h][w] = 0 # type: ignore

c = [(-1,0),(0,-1),(0,1),(1,0)]

ans = 0
while d:
    h, w = d.popleft()
    ans += 1
    if glid[h][w] == D:
        continue
    for dh, dw in c:
        if glid[h+dh][w+dw] == '.':
            d.append((h+dh,w+dw))
            glid[h+dh][w+dw] = glid[h][w] + 1

print(ans)