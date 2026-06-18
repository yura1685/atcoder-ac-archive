import heapq

N, D = map(int,input().split())
job = [tuple(map(int,input().split())) for _ in range(N)]
job.sort(reverse=True)

hq = []
heapq.heapify(hq)

ans = 0
for day in range(1,D+1):
    while job and job[-1][0] == day:
        x, y = job.pop()
        heapq.heappush(hq,-y)
    Y = heapq.heappop(hq) if hq else 0
    ans -= Y

print(ans)