H, W, N = map(int,input().split())
snow = [[0]*(W) for _ in range(H)]

for _ in range(N):
    a, b, c, d = map(int,input().split())
    for h in range(a,c+1):
        snow[h-1][b-1] += 1
        if d < W:
            snow[h-1][d] -= 1

for h in range(H):
    for w in range(W-1):
        snow[h][w+1] += snow[h][w]

for x in snow:
    print(*x)