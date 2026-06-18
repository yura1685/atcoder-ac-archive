import heapq

N, K = map(int,input().split())
A = list(map(int,input().split()))

hq = [0]
heapq.heapify(hq)
s = set()
cnt = 0

while cnt <= K:
    x = heapq.heappop(hq)
    if cnt == K:
        exit(print(x))
    cnt += 1
    for a in A:
        if (x+a) not in s:
            s.add(x+a)
            heapq.heappush(hq,x+a)
