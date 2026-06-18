from atcoder.lazysegtree import LazySegTree

inf = float('inf')
N, M = map(int,input().split())
L = [0] * N

def plus(x, y):
    return x + y

lazy_segtree = LazySegTree(min, inf, plus, plus, 0, L)

Q = []

for _ in range(M):
    s, t = map(int,input().split())
    lazy_segtree.apply(s-1,t,1)
    Q.append((s,t))

ans = []

for i in range(M):
    s, t = Q[i]
    if lazy_segtree.prod(s-1,t) > 1:
        ans.append(i+1)

print(len(ans))
for a in ans:
    print(a)