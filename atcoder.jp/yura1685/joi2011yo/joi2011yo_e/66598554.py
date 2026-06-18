from collections import deque
from copy import deepcopy

H, W, N = map(int,input().split())
glid = [list('X'+input()+'X') for _ in range(H)]
glid = [['X']*(W+2)] + glid + [['X']*(W+2)]
c = [(-1,0),(0,-1),(0,1),(1,0)]

def route(s,g,maze):
    sh, sw = s
    gh, gw = g
    maze[sh][sw] = 0
    d = deque([(sh,sw)])
    while True:
        h, w = d.popleft()
        for dh, dw in c:
            if h+dh == gh and w+dw == gw:
                return maze[h][w]+1
            if type(maze[h+dh][w+dw]) == str and maze[h+dh][w+dw] != 'X':
                maze[h+dh][w+dw] = maze[h][w]+1
                d.append((h+dh,w+dw))

cheese = ['']*(N+1)
for h in range(H+1):
    for w in range(W+1):
        if glid[h][w] in '.X':
            continue
        if glid[h][w] == 'S':
            cheese[0] = (h,w)
        else:
            cheese[int(glid[h][w])] = (h,w)

ans = 0
for i in range(N):
    h = deepcopy(glid)
    ans += route(cheese[i],cheese[i+1],h)
print(ans)