from atcoder.segtree import SegTree

def op(x, y): return x + y
e = 0
inf = 1 << 20

def solve():
    N, K = map(int, input().split())
    S = [1 if s == '1' else 0 if s == '?' else -inf for s in input()]
    M = S.count(1)
    ST = SegTree(op, e, S)
    cnt = 0
    for i in range(N-K+1):
        wa = ST.prod(i, i+K)
        if wa == M:
            cnt += 1
    print('Yes' if cnt == 1 else 'No')

for _ in range(int(input())):
    solve()