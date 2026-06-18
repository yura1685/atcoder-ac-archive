from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int,input().split()))
def plus(x,y): return x + y
segtree = SegTree(plus, 0, A)

for _ in range(Q):
    q, a, b = map(int,input().split())
    if q == 0:
        n = segtree.get(a)
        segtree.set(a, b+n)
    else:
        print(segtree.prod(a,b))