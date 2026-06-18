from collections import defaultdict
from atcoder.dsu import DSU

N = int(input())
d = defaultdict(int)
cnt = 1
g = DSU(2*N+1)
for _ in range(N):
    S, T = input().split()
    if d[S] == 0:
        d[S] = cnt
        cnt += 1
    if d[T] == 0:
        d[T] = cnt
        cnt += 1
    if g.same(d[S],d[T]):
        print('No')
        exit()
    g.merge(d[S],d[T])
    
print('Yes')