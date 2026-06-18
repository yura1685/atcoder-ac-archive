from heapq import heapify, heappop, heappush
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
A = sorted(map(int,input().split()), reverse=True)
B = sorted(map(int,input().split()), reverse=True)
C = sorted(map(int,input().split()), reverse=True)

hq = []
heapify(hq)

S = set()
def add(i, j, k):
    if i < N and j < N and k < N and (i, j, k) not in S:
        S.add((i,j,k))
        heappush(hq, (-A[i]*B[j]-B[j]*C[k]-C[k]*A[i], i, j, k))

add(0,0,0)
while K:
    K -= 1
    s, i, j, k = heappop(hq)
    if not K:
        print(-s)
    add(i+1, j, k)
    add(i, j+1, k)
    add(i, j, k+1)
