from atcoder.lazysegtree import LazySegTree

N = int(input())
A = list(map(int, input().split()))
mod = 998244353

def op(a, b):
    a_size, a_sum = a
    b_size, b_sum = b
    return (a_size + b_size, (a_sum + b_sum) % mod)
_id = 1 << 61
def mapp(f, x):
    if f == _id: return x
    x_size, x_sum = x
    return (x_size, f*x_size)
def comp(f, g): return g if f == _id else f

LST = LazySegTree(op, (0, 0), mapp, comp, _id, [(1, 0) for _ in range(N)])

for i in reversed(range(N-1)):
    a = A[i]
    inv = pow(a, -1, mod)
    S = LST.prod(i + 1, i + a + 1)[1]
    LST.set(i, (1, (a + 1 + S) * inv % mod))

print(LST.get(0)[1])