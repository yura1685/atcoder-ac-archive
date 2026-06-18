from heapq import heapify, heappop, heappush

N = int(input())
A = list(map(int,input().split()))
hq = A[:N]
S = sum(hq)
F = [0] * (N+1)
F[0] = S

heapify(hq)
for i in range(N):
    heappush(hq, A[N+i])
    m = heappop(hq)
    S += A[N+i] - m
    F[i+1] = S

hq = [-a for a in A[2*N:]]
S = sum(hq)
B = [0] * (N+1)
B[0] = S
heapify(hq)
for i in range(N):
    heappush(hq, -A[-N-1-i])
    M = heappop(hq)
    S -= A[-N-1-i] + M
    B[i+1] = S
B = [-b for b in B[::-1]]

print(max(F[i] - B[i] for i in range(N+1)))