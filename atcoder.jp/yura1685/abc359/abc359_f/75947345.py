import heapq

N = int(input())
A = list(map(int, input().split()))
L = []
for a in A:
    heapq.heappush(L, (3*a, a, 1, a))
deg = N - 2

while deg:
    diff, d2a, d, a = heapq.heappop(L)
    nex = d2a + (2*d + 1) * a
    diff = (2*d + 3) * a
    heapq.heappush(L, (diff, nex, d + 1, a))
    deg -= 1

print(sum(x[1] for x in L))