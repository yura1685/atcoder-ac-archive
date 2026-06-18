from heapq import heappush, heappop

X, Y, Z, K = map(int,input().split())
A = sorted(map(int,input().split()), reverse=True)
B = sorted(map(int,input().split()), reverse=True)
C = sorted(map(int,input().split()), reverse=True)
hq = []
heappush(hq, (-A[0]-B[0]-C[0],0,0,0))
visited = set()
visited.add((0,0,0))

for _ in range(K):
    n, i, j, k = heappop(hq)
    print(-n)

    if i + 1 < X and (i+1,j,k) not in visited:
        heappush(hq,(-A[i+1]-B[j]-C[k],i+1,j,k))
        visited.add((i+1,j,k))
    if j + 1 < Y and (i,j+1,k) not in visited:
        heappush(hq,(-A[i]-B[j+1]-C[k],i,j+1,k))
        visited.add((i,j+1,k))
    if k + 1 < Z and (i,j,k+1) not in visited:
        heappush(hq,(-A[i]-B[j]-C[k+1],i,j,k+1))
        visited.add((i,j,k+1))