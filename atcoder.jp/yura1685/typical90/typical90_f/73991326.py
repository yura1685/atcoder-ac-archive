from atcoder.segtree import SegTree

N, K = map(int, input().split())
S = [(s, i) for i, s in enumerate(input())]

def op(x, y):
    xs, xi = x
    ys, yi = y
    if xs < ys: return x
    if ys < xs: return y
    return (xs, min(xi, yi))

st = SegTree(op, ('|', 0), S)

l = 0
ans = []
for _ in range(K):
    s, i = st.prod(l, N-K+1+_)
    ans.append(s)
    l = i + 1

print(''.join(ans))