from sys import setrecursionlimit
setrecursionlimit(10**8)

H, W, K = map(int, input().split())
maze = [list(input()) for _ in range(H)]
c = [(-1,0),(0,-1),(0,1),(1,0)]
ans = 0

def route(h, w, step):
    global ans
    if step == K:
        ans += 1
        return
    for dh, dw in c:
        nh, nw = h + dh, w + dw
        if 0 <= nh < H and 0 <= nw < W and maze[nh][nw] == '.':
            maze[nh][nw] = '#'
            route(nh, nw, step + 1)
            maze[nh][nw] = '.'

for i in range(H):
    for j in range(W):
        if maze[i][j] == '.':
            maze[i][j] = '#'
            route(i, j, 0)
            maze[i][j] = '.'

print(ans)
