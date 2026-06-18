H, W, N, M = map(int,input().split())
U = [[0]*W for _ in range(H)]
D = [[0]*W for _ in range(H)]
R = [[0]*W for _ in range(H)]
L = [[0]*W for _ in range(H)]

for _ in range(N):
    a, b = map(int,input().split())
    a, b = a-1, b-1
    U[a][b] = 1
    D[a][b] = 1
    R[a][b] = 1
    L[a][b] = 1

for _ in range(M):
    c, d = map(int,input().split())
    c, d = c-1, d-1
    U[c][d] = -1
    D[c][d] = -1
    R[c][d] = -1
    L[c][d] = -1

for h in range(H-1,0,-1):
    for w in range(W):
        if U[h][w] == 1 and U[h-1][w] == 0:
            U[h-1][w] = 1

for h in range(H-1):
    for w in range(W):
        if D[h][w] == 1 and D[h+1][w] == 0:
            D[h+1][w] = 1

for w in range(W-1):
    for h in range(H):
        if R[h][w] == 1 and R[h][w+1] == 0:
            R[h][w+1] = 1

for w in range(W-1,0,-1):
    for h in range(H):
        if L[h][w] == 1 and L[h][w-1] == 0:
            L[h][w-1] = 1

ans = 0
for h in range(H):
    for w in range(W):
        if 1 in (U[h][w],D[h][w],R[h][w],L[h][w]):
            ans += 1
        
print(ans)