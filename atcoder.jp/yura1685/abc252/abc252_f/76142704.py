import heapq

N, L = map(int, input().split())
A = list(map(int, input().split()))
B = L - sum(A)
if B: A.append(B)
heapq.heapify(A)
ans = 0
while len(A) > 1:
    u = heapq.heappop(A)
    v = heapq.heappop(A)
    ans += u + v
    heapq.heappush(A, u + v)
print(ans)