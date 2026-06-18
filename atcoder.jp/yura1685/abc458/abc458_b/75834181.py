H, W = map(int, input().split())
L = [[0]*W for _ in range(H)]
for h in range(H):
    for w in range(W):
        if h-1 >= 0:
            L[h][w] += 1
        if w-1 >= 0:
            L[h][w] += 1
        if h+1 < H:
            L[h][w] += 1
        if w+1 < W:
            L[h][w] += 1

for l in L:
    print(*l)