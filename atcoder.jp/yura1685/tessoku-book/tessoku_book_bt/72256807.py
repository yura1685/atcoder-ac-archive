H, W, K = map(int,input().split())
c = []
for _ in range(H):
    n = input()
    n = n.replace('.','0')
    n = n.replace('#','1')
    c.append(int(n,2))

from itertools import product

ans = 0
for P in product([0,1],repeat=H):
    if sum(P) > K: continue
    x = c.copy()
    for p in range(H):
        if not P[p]: continue
        x[p] = (1 << W) - 1
    cnt = sum(x[h].bit_count() for h in range(H))
    y = sorted([H - sum((x[h] & (1 << w)) >> w for h in range(H)) for w in range(W-1,-1,-1)], reverse=True)
    ans = max(ans, cnt + sum(y[:K-sum(P)]))

print(ans)