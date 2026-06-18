from collections import deque

H, W = map(int,input().split())

S = ['#'*(W+2)] + ['#'+input()+'#' for _ in range(H)] + ['#'*(W+2)]
dire = [(-1,0),(0,-1),(0,1),(1,0)]

def maze(x,y):
    c = [[-1]*(W+2) for _ in range(H+2)]
    c[x][y] = 0
    d = deque([(x,y)])
    while d:
        h, w = d.popleft()
        for dh, dw in dire:
            if S[h+dh][w+dw] == '.' and c[h+dh][w+dw] == -1:
                c[h+dh][w+dw] = c[h][w] + 1
                d.append((h+dh,w+dw))
    M = 0
    for i in c:
        M = max(M,max(i))

    return M

ans = 0
for i in range(1,H+1):
    for j in range(1,W+1):
        if S[i][j] == '.':
            ans = max(ans,maze(i,j))
print(ans)