from heapq import *

N = int(input())
L = [tuple(map(int,input().split())) for _ in range(N)]
L += [(i,101) for i in range(1,N+1)]
L.sort()

hq = []
heapify(hq)

ans = 0
for A, B in L:
    if B < 101:
        heappush(hq,-B)
    else:
        X = heappop(hq) if hq else 0
        ans -= X
        print(ans)