from atcoder.segtree import SegTree

N, Q = map(int,input().split())
S = input()
A = [1 if S[i] != S[i+1] else 0 for i in range(N-1)]
def op(x,y): return x+y
seg = SegTree(op, 0, A)

for _ in range(Q):
    i, l, r = map(int,input().split())
    l, r = l-1, r-1
    if i == 1:
        if l > 0:
            seg.set(l-1, 1 - seg.get(l-1))
        if r < N-1:
            seg.set(r, 1 - seg.get(r))
    else:
        if seg.prod(l,r) == r-l:
            print('Yes')
        else:
            print('No')