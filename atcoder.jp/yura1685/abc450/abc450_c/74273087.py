from atcoder.dsu import DSU
from collections import defaultdict

H, W = map(int, input().split())
S = [input() for _ in range(H)]
uf = DSU(H*W)
def f(x, y): return x*W + y
for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            continue
        if h > 0 and S[h-1][w] == '.':
            uf.merge(f(h,w), f(h-1,w))
        if w > 0 and S[h][w-1] == '.':
            uf.merge(f(h,w), f(h,w-1))

ans = defaultdict(bool)

for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            continue
        u = uf.leader(f(h,w))
        if h == 0 or h == H-1 or w == 0 or w == W-1:
            ans[u] = False
        else:
            if u in ans:
                continue
            ans[u] = True

print(sum(ans.values()))