from collections import defaultdict
from bisect import bisect_left, bisect_right
from atcoder.segtree import SegTree

N, M = map(int, input().split())
dl = defaultdict(list)
dr = defaultdict(list)
dc = defaultdict(int)

inf = 10 ** 18
minR = [inf] * (N+2)

for _ in range(M):
    L, R = map(int, input().split())
    dl[L].append(R)
    dr[R].append(L)
    dc[(L, R)] += 1
    if R < minR[L]:
        minR[L] = R

for lst in dl.values(): lst.sort()
for lst in dr.values(): lst.sort()

st = SegTree(min, inf, minR)

Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    x = None
    if s in dl:
        lst = dl[s]
        l = bisect_left(lst, t)
        if l > 0:
            x = lst[l-1]
    
    y = None
    if t in dr:
        lst = dr[t]
        r = bisect_right(lst, s)
        if r < len(lst):
            y = lst[r]
    
    if x is not None and y is not None and y <= x + 1:
        print('Yes')
        continue

    if dc[(s, t)] > 0:
        if dc[(s, t)] >= 2 or x is not None or y is not None:
            print('Yes')
            continue
        
        if s + 1 <= t - 1:
            if st.prod(s+1, t) <= t-1:
                print('Yes')
                continue
    
    print('No')