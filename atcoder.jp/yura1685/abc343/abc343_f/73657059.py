from atcoder.segtree import SegTree
from collections import defaultdict

N, Q = map(int,input().split())
A = list(map(int,input().split()))

def op(x, y):
    v1x, c1x, v2x, c2x = x
    v1y, c1y, v2y, c2y = y
    if v1x == v1y:
        res_v1, res_c1 = v1x, c1x + c1y
        if v2x == v2y:
            res_v2, res_c2 = v2x, c2x + c2y
        elif v2x > v2y:
            res_v2, res_c2 = v2x, c2x
        else:
            res_v2, res_c2 = v2y, c2y
    elif v1x > v1y:
        res_v1, res_c1 = v1x, c1x
        if v2x == v1y:
            res_v2, res_c2 = v2x, c2x + c1y
        elif v2x > v1y:
            res_v2, res_c2 = v2x, c2x
        else:
            res_v2, res_c2 = v1y, c1y
    else:
        res_v1, res_c1 = v1y, c1y
        if v1x == v2y:
            res_v2, res_c2 = v1x, c1x + c2y
        elif v1x > v2y:
            res_v2, res_c2 = v1x, c1x
        else:
            res_v2, res_c2 = v2y, c2y
            
    return (res_v1, res_c1, res_v2, res_c2)



e = (-1,0,-2,0)
X = [(a,1,-1,0) for a in A]
st = SegTree(op, e, X)

for _ in range(Q):
    q, p, x = map(int,input().split())
    if q == 1:
        st.set(p-1, (x,1,-1,0))
    else:
        print(st.prod(p-1,x)[3])