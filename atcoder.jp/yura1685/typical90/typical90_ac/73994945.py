from atcoder.lazysegtree import LazySegTree
def op(a, b): return max(a, b)
_e = -(1<<60) # INFの値は適宜
def mapp(f, x): return x if f == _id else f
def comp(f, g): return g if f == _id else f
_id = 1<<61

W, N = map(int, input().split())
S = LazySegTree(op, _e, mapp, comp, _id, [0] * W) # vに初期化の配列

for _ in range(N):
    L, R = map(int, input().split())
    n = S.prod(L-1, R)
    print(n + 1)
    S.apply(L-1, R, n + 1)