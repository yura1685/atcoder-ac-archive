from atcoder.segtree import SegTree

N, Q = map(int,input().split())
A = list(map(int,input().split()))

segtree = SegTree(max, -1, A)

for _ in range(Q):
    t, x, y = map(int,input().split())
    if t == 1:
        segtree.set(x-1, y)
    elif t == 2:
        print(segtree.prod(x-1,y))
    else:
        print(segtree.max_right(x-1, lambda v: v < y) + 1)