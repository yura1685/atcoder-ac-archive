from itertools import product

H, W, K = map(int,input().split())

c = [input() for _ in range(H)]

re = list(product([0,1],repeat=W))
gy = list(product([0,1],repeat=H))

ans = 0
for r in re:
    for g in gy:
        hoge = 0
        for h in range(H):
            for w in range(W):
                if c[h][w] == '#' and g[h] == 0 and r[w] == 0:
                    hoge += 1
        if hoge == K:
            ans += 1

print(ans)