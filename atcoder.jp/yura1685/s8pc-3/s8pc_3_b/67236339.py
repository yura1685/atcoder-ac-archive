from copy import deepcopy
from more_itertools import run_length

H, W, K = map(int,input().split())
yura = [list(map(int,input())) for _ in range(H)]

def pop(x,y):
    glid = deepcopy(yura)
    glid[x][y] = 0
    for h in range(x,0,-1):
        glid[h][y], glid[h-1][y] = glid[h-1][y], glid[h][y]
    score = 0
    turn = 0
    while True:
        X = 0
        for h in range(H):
            G = []
            for num, cnt in run_length.encode(glid[h]):
                if cnt >= K:
                    X += 2**turn * (num*cnt)
                    G += [0]*cnt
                else:
                    G += [num]*cnt
            glid[h] = G
        if X == 0:
            break
        turn += 1
        score += X
        for w in range(W):
            while True:
                swap = 0
                for h in range(H-1):
                    if glid[h][w] != 0 and glid[h+1][w] == 0:
                        swap += 1
                        glid[h][w], glid[h+1][w] = glid[h+1][w], glid[h][w]
                if swap == 0:
                    break
    return score

ans = [pop(*divmod(i,W)) for i in range(H*W)]
print(max(ans))