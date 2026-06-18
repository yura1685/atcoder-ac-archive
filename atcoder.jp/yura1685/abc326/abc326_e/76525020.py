from atcoder.lazysegtree import LazySegTree

mod = 998244353
N = int(input())
A = list(map(int, input().split()))

def op(ele1, ele2):
    return (ele1 + ele2) % mod

def mapping(func, ele):
    return func + ele

def composition(func_upper, func_lower):
    return func_upper + func_lower

S = LazySegTree(op, 0, mapping, composition, 0, [0] * N)

inv = pow(N, -1, mod)
p = inv
for i in range(N):
    S.apply(i, N, p)
    p = S.get(i) * inv % mod

ans = 0
for i in range(N):
    ans += A[i] * S.get(i)
    ans %= mod

print(ans)