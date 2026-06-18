from atcoder.lazysegtree import LazySegTree

mod = 998244353

def op(s1, s2):
    return ((s1[0] + s2[0]) % mod, s1[1] + s2[1])

e = (0, 0)

def mapping(f, s):
    return ((f[0] * s[0] + f[1] * s[1]) % mod, s[1])

def composition(fn, fo):
    return (fn[0] * fo[0] % mod, (fn[0] * fo[1] + fn[1]) % mod)

id_ = (1, 0)

N, M = map(int, input().split())
A = [(int(x) % mod, 1) for x in input().split()]

lst = LazySegTree(op, e, mapping, composition, id_, A)

for _ in range(M):
    L, R, X = map(int, input().split())
    L -= 1
    S = R - L
    inv_S = pow(S, -1, mod)
    a = (S-1) * inv_S % mod
    b = inv_S * X % mod
    lst.apply(L, R, (a, b))

for i in range(N):
    print(lst.get(i)[0])