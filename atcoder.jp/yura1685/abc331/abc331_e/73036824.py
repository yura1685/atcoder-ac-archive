from heapq import heappush, heappop
def f(n): return -int(n)
N, M, L = map(int, input().split())
A_in = list(map(f,input().split()))
B_in = list(map(f,input().split()))
A = sorted((n,i) for i, n in enumerate(A_in))
B = sorted((n,i) for i, n in enumerate(B_in))

S = set()
for _ in range(L):
    c, d = map(int,input().split())
    S.add((c-1, d-1))

hq = []
heappush(hq, (A[0][0]+B[0][0], 0, 0))
visited = set([(0,0)])

while hq:
    s, k, l = heappop(hq)
    if (A[k][1], B[l][1]) not in S:
        exit(print(-s))
    if k + 1 < N and (k+1, l) not in visited:
        visited.add((k+1,l))
        heappush(hq, (A[k+1][0]+B[l][0], k+1, l))
    if l + 1 < M and (k, l+1) not in visited:
        visited.add((k,l+1))
        heappush(hq, (A[k][0]+B[l+1][0], k, l+1))
