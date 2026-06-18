from sortedcontainers import SortedSet

N = int(input())
P = []
for i in range(2*N):
    x, y = map(int,input().split())
    P.append((x,y,i//N))

P.sort()
SS = SortedSet()

ans = 0
for _, y, col in P:
    if col == 0:
        SS.add(y)
    elif SS:
        n = SS.bisect_left(y)
        if n:
            z = SS.pop(n-1)
            ans += 1

print(ans)