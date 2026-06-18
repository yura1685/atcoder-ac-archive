from heapq import *

N = int(input())
Q = sorted(tuple(map(int,input().split())) for _ in range(N))
hq = []
heapify(hq)
cnt = 0
t = 1
ans = 0
while 1:
    while cnt < N and Q[cnt][0] == t:
        heappush(hq,Q[cnt][0]+Q[cnt][1])
        cnt += 1
    while hq:
        p = heappop(hq)
        if t <= p:
            ans += 1
            t += 1
            break
    if not hq:
        if cnt == N:
            break
        t = Q[cnt][0]


print(ans)