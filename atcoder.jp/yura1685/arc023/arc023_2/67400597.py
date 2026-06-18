H, W, D = map(int,input().split())

glid = [list(map(int,input().split())) for _ in range(H)]

ans = 0
for h in range(H):
    for w in range(W):
        if h+w <= D and (h+w) % 2 == D % 2:
            ans = max(ans,glid[h][w])

print(ans)