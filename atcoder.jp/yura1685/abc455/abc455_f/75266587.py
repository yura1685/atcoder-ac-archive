from atcoder.lazysegtree import LazySegTree

mod = 998244353
inv = pow(2, -1, mod)
N, Q = map(int, input().split())
A = [(0, 0, 1)] * N

def op(x, y):
    return ((x[0]+y[0]) % mod, (x[1]+y[1]) % mod, (x[2] + y[2]) % mod)

e = (0, 0, 0)

def mapping(func, ele):
    s, s2, n = ele
    if func == 0:
        return ele
    new_s2 = (s2 + 2*func*s + n*func*func) % mod
    new_s = (s + n * func) % mod
    return (new_s, new_s2, n)

def composition(func_upper, func_lower):
    return (func_upper + func_lower) % mod

id = 0

lst = LazySegTree(op, e, mapping, composition, id, A)

for _ in range(Q):
    l, r, a = map(int, input().split())
    lst.apply(l-1, r, a)
    s, s2, n = lst.prod(l-1, r)
    ans = (s*s - s2) * inv % mod
    print(ans)