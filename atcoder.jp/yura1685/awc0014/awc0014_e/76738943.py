from atcoder.lazysegtree import LazySegTree
def op(a, b):
    a_size, a_sum = a
    b_size, b_sum = b
    return (a_size+b_size, a_sum+b_sum)
_e = (0, 0)
def mapp(f, x):
    x_size, x_sum = x
    return (x_size, x_sum+f*x_size)
def comp(f, g): return f+g
_id = 0
N, Q = map(int, input().split())
C = list(map(int, input().split()))
vv = [(1, vi) for vi in C]
lst = LazySegTree(op, _e, mapp, comp, _id, vv)
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        l, r, v = q[1:]
        lst.apply(l-1, r, v)
    else:
        l, r = q[1:]
        print(lst.prod(l-1, r)[1])