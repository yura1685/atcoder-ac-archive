H, W = map(int,input().split())

c = [list(map(int,input().split())) for _ in range(10)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j], c[i][k]+c[k][j])

wall = [list(map(int,input().split())) for _ in range(H)]

magic = 0
for h in range(H):
    for w in range(W):
        if wall[h][w] == -1:
            continue
        magic += c[wall[h][w]][1]

print(magic)