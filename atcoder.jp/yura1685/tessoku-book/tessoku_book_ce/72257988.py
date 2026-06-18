from atcoder.segtree import SegTree

N = int(input())
A = list(map(int,input().split()))
def op(x, y): return x+y
st = SegTree(op, 0, A)

Q = int(input())
for _ in range(Q):
    l, r = map(int,input().split())
    n = r-l+1
    cnt = st.prod(l-1,r)
    if 2*cnt == n: print('draw')
    if 2*cnt <  n: print('lose')
    if 2*cnt >  n: print('win')