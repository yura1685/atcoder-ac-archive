from atcoder.lazysegtree import LazySegTree

def plus(x, y): return x + y

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
lst = LazySegTree(plus, 0, plus, plus, 0, A)

for b in B:
    ball = lst.get(b)
    lst.set(b, 0)
    lst.apply(0, N, ball//N)
    ball %= N
    migi = N - b - 1
    if ball <= migi:
        lst.apply(b+1, b+1+ball, 1)
    else:
        lst.apply(b+1, N, 1)
        ball -= migi
        lst.apply(0, ball, 1)

print(*[lst.get(p) for p in range(N)])