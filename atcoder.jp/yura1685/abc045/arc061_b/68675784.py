H, W, N = map(int,input().split())
s = [set() for _ in range(10)]
c = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
for _ in range(N):
    h, w = map(int,input().split())
    for dh, dw in c:
        if not (1 < h + dh < H and 1 < w + dw < W):
            continue
        tp = (h + dh, w + dw)
        for i in range(1,9):
            if tp in s[i]:
                s[i+1].add(tp)
                s[i].discard(tp)
                break
        else:
            s[1].add(tp)

ans = [0]*10
for i in range(9,0,-1):
    ans[i] = len(s[i])
ans[0] = (H-2)*(W-2) - sum(ans)

for i in ans:
    print(i)