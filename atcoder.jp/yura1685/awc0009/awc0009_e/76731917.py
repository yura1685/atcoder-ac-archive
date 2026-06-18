from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))
smax = SegTree(max, - 10 ** 18, A)
smin = SegTree(min, 10 ** 18, A)
for _ in range(Q):
    L, R = map(int, input().split())
    print(smax.prod(L-1, R) - smin.prod(L-1, R))