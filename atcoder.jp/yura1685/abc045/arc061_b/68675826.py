from collections import defaultdict
H, W, N = map(int,input().split())
d = defaultdict(int)
c = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
for _ in range(N):
    h, w = map(int,input().split())
    for dh, dw in c:
        if not (1 < h + dh < H and 1 < w + dw < W):
            continue
        tp = (h + dh, w + dw)
        d[tp] += 1

L = list(d.values())
ans = [L.count(i) for i in range(1,10)]
print((H-2)*(W-2) - sum(ans))
for i in ans: print(i)