from atcoder.segtree import SegTree

N = int(input())
S = input()
X = [1 << (ord(s)-97) for s in S]

def op(x, y): return x | y
seg = SegTree(op,0,X)

Q = int(input())
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        i, c = int(q[1])-1, ord(q[2])-97
        seg.set(i, 1 << c)
    else:
        l, r = int(q[1])-1, int(q[2])
        N = seg.prod(l,r)
        print(N.bit_count())