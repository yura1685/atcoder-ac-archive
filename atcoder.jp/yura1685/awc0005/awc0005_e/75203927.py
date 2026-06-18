from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))
seg = SegTree(max, 0, A)
for _ in range(Q):
    L, R = map(int, input().split())
    print(seg.prod(L-1, R))