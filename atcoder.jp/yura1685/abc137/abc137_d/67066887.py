import heapq

N, M = map(int,input().split())

job = [[] for _ in range(M+1)]
for _ in range(N):
    A, B = map(int,input().split())
    if A > M:
        continue
    job[A].append(B)

a = []
heapq.heapify(a)

money = 0
day = 0
for l in job:
    if l:
        for c in l:
            heapq.heappush(a, -c)
    if a:
        money -= heapq.heappop(a)
        day += 1

print(money)