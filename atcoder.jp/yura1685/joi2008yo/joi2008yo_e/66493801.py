from itertools import product

H, W = map(int,input().split())
senbei = [list(map(int,input().split())) for _ in range(H)]
iebnes = list(zip(*senbei))
C = list(product([0,1],repeat=H))

ans = 0
for c in C:
    bake = 0
    for z in iebnes:
        cnt = 0
        for i in range(H):
            if c[i] == 1:
                cnt += 1-z[i]
            else:
                cnt += z[i]
        bake += max(cnt, H-cnt)
    ans = max(ans, bake)
print(ans)