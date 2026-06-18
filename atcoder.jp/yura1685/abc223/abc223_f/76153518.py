from atcoder.lazysegtree import LazySegTree
def op(a, b): return min(a, b)
e = 1 << 60 # INFの値は適宜
def mapp(f, x): return f+x
def comp(f, g): return f+g
_id = 0

N, Q = map(int, input().split())
S = list(input())
L = [0] * N
for i, s in enumerate(S):
    if s == '(':
        L[i] = 1
    else:
        L[i] = -1
for i in range(N-1):
    L[i+1] += L[i]

lst = LazySegTree(op, e, mapp, comp, _id, L) 

for _ in range(Q):
    q, l, r = map(int, input().split())
    l, r = l-1, r-1
    if q == 1:
        if S[l] == S[r]: continue
        if S[l] == '(': lst.apply(l, r, -2)
        else: lst.apply(l, r, 2)
        S[l], S[r] = S[r], S[l]
    else:
        n = lst.get(l)
        if S[l] == ')': print('No')
        elif lst.prod(l, r+1) >= n - 1 and lst.get(r) == n - 1:
            print('Yes')
        else:
            print('No')