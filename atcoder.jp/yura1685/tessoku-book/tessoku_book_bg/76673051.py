from atcoder.segtree import SegTree

N, Q = map(int, input().split())
def op(a, b): return a + b
S = SegTree(op, 0, [0]*N)
for _ in range(Q):
    q, a, b = map(int, input().split())
    if q == 1:
        S.set(a-1, b)
    else:
        print(S.prod(a-1, b-1))