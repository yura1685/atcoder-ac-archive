W, H, N = map(int,input().split())
glid = [[0]*W for _ in range(H)]

for _ in range(N):
    x, y, a = map(int,input().split())
    if a == 1:
        for h in range(H):
            for w in range(x):
                glid[h][w] = 1
    if a == 2:
        for h in range(H):
            for w in range(W-x):
                glid[h][-1-w] = 1
    if a == 3:
        for h in range(y):
            for w in range(W):
                glid[-1-h][w] = 1
    if a == 4:
        for h in range(H-y):
            for w in range(W):
                glid[h][w] = 1

ans = 0
for l in glid:
    ans += l.count(0)

print(ans)