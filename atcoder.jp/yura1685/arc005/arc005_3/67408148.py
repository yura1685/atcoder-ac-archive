from collections import deque

H, W = map(int,input().split())
g = [['=']*(W+2)]+[list('='+input()+'=') for _ in range(H)]+[['=']*(W+2)]

xy = [(-1,0),(0,-1),(0,1),(1,0)]

for h in range(H+2):
    for w in range(W+2):
        if g[h][w] == 's':
            sh, sw = h, w
            d = deque([(sh,sw)])
            break

m = [[float('inf')]*(W+2) for _ in range(H+2)]
m[sh][sw] = 0

while d:
    h, w = d.popleft()
    for dh, dw in xy:
        if g[h+dh][w+dw] =='g':
            if m[h][w] <= 2:
                print('YES')
                exit()
        elif g[h+dh][w+dw] == '.':
            if m[h+dh][w+dw] > m[h][w]:
                m[h+dh][w+dw] = m[h][w]
                d.appendleft((h+dh,w+dw))
        elif g[h+dh][w+dw] == '#':
            if m[h+dh][w+dw] > m[h][w]+1:
                m[h+dh][w+dw] = m[h][w]+1
                d.append((h+dh,w+dw))

print('NO')