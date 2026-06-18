H, W, N, h, w = map(int,input().split())
col = [[W, -1, H, -1] for _ in range(N+1)]
A = [list(map(int,input().split())) for _ in range(H)]

for i in range(H):
    for j in range(W):
        c = A[i][j]
        col[c][0] = min(col[c][0], j)
        col[c][1] = max(col[c][1], j)
        col[c][2] = min(col[c][2], i)
        col[c][3] = max(col[c][3], i)

base = sum(X[0] != W for X in col)

for u in range(H-h+1):
    for l in range(W-w+1):
        d = u + h - 1
        r = l + w - 1
        ans = base
        for c in range(N+1):
            L, R, U, D = col[c]
            if l <= L <= R <= r and u <= U <= D <= d:
                ans -= 1
        print(ans, end=' ')
    print()