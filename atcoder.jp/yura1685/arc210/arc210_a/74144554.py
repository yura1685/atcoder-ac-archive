from atcoder.lazysegtree import LazySegTree
def plus(x, y): return x+y
N, Q = map(int, input().split())
seg = LazySegTree(plus, 0, plus, plus, 0, list(range(N+1)))
ans = N*(N+1)//2
for _ in range(Q):
    i, x = map(int, input().split())
    n = seg.get(i)
    seg.set(i, n+x)
    if i < N:
        m = seg.get(i+1)
        if n + x < m: continue
        else:
            y = n + x - m + 1
            seg.apply(i+1, N+1, y)
            ans += y * (N - i)
print(ans)