import heapq

N, Q = map(int,input().split())
IN = [1] * N
hq = []
heapq.heapify(hq)
for i in range(N):
    heapq.heappush(hq,(i,1))

for _ in range(Q):
    X, Y = map(int,input().split())
    X, Y = X-1, Y-1
    cnt = 0
    while hq and hq[0][0] <= X:
        os, c = heapq.heappop(hq)
        IN[os] = 0
        cnt += c
    print(cnt)
    IN[Y] += cnt
    heapq.heappush(hq,(Y,cnt))