from atcoder.lazysegtree import LazySegTree

N, Q = map(int, input().split())
Query = [tuple(map(int, input().split())) for _ in range(Q)]
sort_C = sorted(Query, key=lambda x: x[2])
sort_L = sorted(Query, key=lambda x: x[0])


flag = False
if sort_L[0][0] > 1:
    flag = True
else:
    cover = 1
    for l, r, _ in sort_L:
        if cover < l:
            flag = True
        else:
            cover = max(cover, r)
    if cover < N:
        flag = True
if flag:
    exit(print(-1))


def op(a, b):
    a_size, a_sum = a
    b_size, b_sum = b
    return (a_size+b_size, a_sum+b_sum)
_e = (0, 0)
def mapp(f, x):
    if f == _id: return x
    x_size, x_sum = x
    return (x_size, f*x_size)
def comp(f, g): return g if f == _id else f
_id = 1<<61
vv = [(1, 1) for _ in range(N)]
LST = LazySegTree(op, _e, mapp, comp, _id, vv)


ans = 0
for l, r, c in sort_C:
    s = LST.prod(l-1, r-1)[1]
    ans += (s + 1) * c
    LST.apply(l-1, r-1, 0)

print(ans)