from collections import deque

H, W = map(int,input().split())

glid = [list('#'+input()+'#') for _ in range(H)]
glid = [['#']*(W+2)] + glid + [['#']*(W+2)]
ans = sum([glid[i].count('.') for i in range(H+2)])

d = deque([(1,1)])
glid[1][1] = 1
c = [(-1,0),(0,-1),(0,1),(1,0)]

while d:
    h, w = d.popleft()
    for dh, dw in c:
        if (h+dh,w+dw) == (H,W):
            glid[H][W] = glid[h][w]+1
            print(ans-glid[H][W])
            exit()
        if glid[h+dh][w+dw] == '.':
            glid[h+dh][w+dw] = glid[h][w]+1
            d.append((h+dh,w+dw))
print(-1)