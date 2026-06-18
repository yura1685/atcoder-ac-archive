H, W, T = map(int,input().split())

glid = [['=']*(W+2)] + [list('='+input()+'=') for _ in range(H)] + [['=']*(W+2)]
c = [(-1,0),(0,-1),(0,1),(1,0)]

for i in range(H+2):
    for j in range(W+2):
        if glid[i][j] == 'S':
            sh, sw = i, j
        if glid[i][j] == 'G':
            gh, gw = i, j

def time(black):
    maze = [[10**10]*(W+2) for _ in range(H+2)]
    maze[sh][sw] = 0
    d = [(0,sh,sw)]
    while d:
        t, h, w = d.pop()
        for dh, dw in c:
            if glid[h+dh][w+dw] in '.G' and maze[h+dh][w+dw] > maze[h][w] + 1:
                maze[h+dh][w+dw] = maze[h][w] + 1
                d.append((maze[h+dh][w+dw],h+dh,w+dw))
            elif glid[h+dh][w+dw] == '#' and maze[h+dh][w+dw] > maze[h][w] + black:
                maze[h+dh][w+dw] = maze[h][w] + black
                d.append((maze[h+dh][w+dw],h+dh,w+dw))
        d.sort(reverse=True)
    return maze[gh][gw]

l, r = 1, T+1
while r-l > 1:
    mid = (r+l)//2
    if time(mid) > T:
        r = mid
    else:
        l = mid

print(l)