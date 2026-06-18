from collections import deque

H, W = map(int,input().split())

glid = [list('#'+input()+'#') for _ in range(H)]
glid = [['#']*(W+2)] + glid + [['#']*(W+2)]

glid[1][1] = 1
d = deque([(1,1,1)])
m = 1
while d != deque():
    h, w, n = d.popleft()
    if glid[h+1][w] == '.':
        glid[h+1][w] = n+1
        d.append((h+1,w,n+1))
        m = n+1
    if glid[h][w+1] == '.':
        glid[h][w+1] = n+1
        d.append((h,w+1,n+1))
        m = n+1
print(m)