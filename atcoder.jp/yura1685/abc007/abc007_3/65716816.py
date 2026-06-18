from collections import deque

R, C = map(int,input().split())
sy, sx = map(int,input().split())
gy, gx = map(int,input().split())


glid = [list(input()) for _ in range(R)]

glid[sy-1][sx-1] = '0'
time = 1
serch = deque([(sy-1,sx),(sy,sx-1),(sy,sx+1),(sy+1,sx)])

while glid[gy-1][gx-1] == '.':
    c = []
    while len(serch) != 0:
        zahyo = serch.popleft()
        y = zahyo[0]
        x = zahyo[1]
        if glid[y-1][x-1] == '.':
            glid[y-1][x-1] = str(time)
            c += [(y-1,x), (y,x-1), (y,x+1), (y+1,x)]
    time += 1
    serch = deque(c)

print(glid[gy-1][gx-1])