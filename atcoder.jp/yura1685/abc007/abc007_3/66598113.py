from collections import deque

R, C = map(int,input().split())
sy, sx = map(int,input().split())
gy, gx = map(int,input().split())

maze = [list(input()) for _ in range(R)]
maze[sy-1][sx-1] = 0

d = deque([(sy, sx)])
c = [(-1,0),(0,-1),(0,1),(1,0)]
while True:
    y, x = d.popleft()
    for dy, dx in c:
        if y+dy == gy and x+dx == gx:
            print(maze[y-1][x-1]+1)
            exit()
        if maze[y+dy-1][x+dx-1] == '.':
            maze[y+dy-1][x+dx-1] = maze[y-1][x-1] + 1
            d.append((y+dy,x+dx))
