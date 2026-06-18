from sys import setrecursionlimit
setrecursionlimit(10**8)

H, W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]

ans = 0

def dfs(lst,n):
    global ans
    res = 0
    for h in range(H):
        for w in range(W):
            if lst[h][w] > 0:
                res ^= lst[h][w]
    for x in range(n,H*W):
        h, w = divmod(x,W)
        if lst[h][w] < 0:
            continue
        lst2 = [[lst[i][j] for j in range(W)] for i in range(H)]
        if w != W-1 and lst[h][w+1] >= 0:
            lst2[h][w], lst2[h][w+1] = -lst2[h][w]-1, -lst2[h][w+1]-1
            dfs(lst2,x)
            lst2[h][w], lst2[h][w+1] = -lst2[h][w]-1, -lst2[h][w+1]-1
        if h != H-1 and lst[h+1][w] >= 0:
            lst2[h][w], lst2[h+1][w] = -lst2[h][w]-1, -lst2[h+1][w]-1
            dfs(lst2,x)
            lst2[h][w], lst2[h+1][w] = -lst2[h][w]-1, -lst2[h+1][w]-1
    ans = max(ans,res)

dfs(A,0)

print(ans)