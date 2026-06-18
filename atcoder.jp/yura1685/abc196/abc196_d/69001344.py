from sys import setrecursionlimit
setrecursionlimit(10**8)
H, W, A, B = map(int,input().split())

glid = [[0]*W for _ in range(H)]

ans = 0
def dfs(X,n,use):
    global ans
    ans += (use == A)
    for x in range(n,H*W):
        h, w = divmod(x,W)
        if X[h][w] == 1:
            continue
        Y = [[X[i][j] for j in range(W)] for i in range(H)]
        if w < W-1 and X[h][w+1] == 0 and use < A:
            Y[h][w], Y[h][w+1] = 1, 1
            dfs(Y,x,use+1)
            Y[h][w], Y[h][w+1] = 0, 0
        if h < H-1 and X[h+1][w] == 0 and use < A:
            Y[h][w], Y[h+1][w] = 1, 1
            dfs(Y,x,use+1)
            Y[h][w], Y[h+1][w] = 0, 0

dfs(glid,0,0)

print(ans)