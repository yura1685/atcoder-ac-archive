from collections import defaultdict

H, W, N = map(int,input().split())
dh, dw = defaultdict(set), defaultdict(set)

for i in range(N):
    h, w = map(int,input().split())
    dh[h].add((w,i))
    dw[w].add((h,i))

ans = [() for _ in range(N)]
check = [0] * N
X, Y = H, W
x, y = 0, 0
while True:
    if dh[X]:
        for w, i in dh[X]:
            if check[i]:
                continue
            check[i] = 1
            ans[i] = (x+1,y+1)
            y += w
            Y -= w 
        dh[X].clear()
    elif dw[Y]:
        for h, i in dw[Y]:
            if check[i]:
                continue
            check[i] = 1
            ans[i] = (x+1,y+1)
            x += h
            X -= h 
        dw[Y].clear()
    else:
        break

for x, y in ans:
    print(x,y)