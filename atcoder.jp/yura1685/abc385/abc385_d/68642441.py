from sortedcontainers import SortedSet
from collections import defaultdict

xy = defaultdict(SortedSet)
yx = defaultdict(SortedSet)

N, M, X, Y = map(int,input().split())

for _ in range(N):
    x, y = map(int,input().split())
    xy[x].add(y)
    yx[y].add(x)

del x, y

ans = 0
for _ in range(M):
    D, C = input().split()
    C = int(C)
    if D == 'U':
        new_Y = Y + C
        L = [y for y in xy[X].irange(Y, new_Y)]
        for y in L:
            xy[X].discard(y)
            yx[y].discard(X)
            ans += 1
        Y = new_Y
    if D == 'D':
        new_Y = Y - C
        L = [y for y in xy[X].irange(new_Y, Y)]
        for y in L:
            xy[X].discard(y)
            yx[y].discard(X)
            ans += 1
        Y = new_Y
    if D == 'R':
        new_X = X + C
        L = [x for x in yx[Y].irange(X, new_X)]
        for x in L:
            yx[Y].discard(x)
            xy[x].discard(Y)
            ans += 1
        X = new_X
    if D == 'L':
        new_X = X - C
        L = [x for x in yx[Y].irange(new_X, X)]
        for x in L:
            yx[Y].discard(x)
            xy[x].discard(Y)
            ans += 1
        X = new_X

print(X,Y,ans)