import heapq

N, M = map(int,input().split())
A = list(map(lambda x:int(x)*(-1), input().split()))

heapq.heapify(A)

for _ in range(M):
    m = heapq.heappop(A)
    heapq.heappush(A, (m+1)//2)

print(-sum(A))