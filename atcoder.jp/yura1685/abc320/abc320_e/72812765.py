import heapq

N, M = map(int,input().split())
who = [i for i in range(N)]
act = [tuple(map(int,input().split())) for _ in range(M)]
get = [0] * N
heapq.heapify(who); heapq.heapify(act)

while act:
    x, y, z = heapq.heappop(act)
    if y == 0:
        heapq.heappush(who,z)
    else:
        if not who:
            continue
        m = heapq.heappop(who)
        get[m] += y
        heapq.heappush(act,(x+z,0,m))

for g in get:
    print(g)