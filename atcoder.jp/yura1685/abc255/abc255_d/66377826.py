import bisect

N, Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

d = 0
for i in range(1,N):
    d += A[i]-A[0]

dis = [0]*N
dis[0] = d

for i in range(1,N):
    dis[i] = dis[i-1] + (A[i]-A[i-1])*(-N+2*i)

for _ in range(Q):
    X = int(input())
    l = bisect.bisect_left(A,X)
    r = bisect.bisect(A,X)
    if l != r:
        print(dis[l])
    else:
        if l == 0:
            print(dis[0]+N*(A[0]-X))
        elif l == N:
            print(dis[-1]+N*(X-A[-1]))
        else:
            print(dis[l-1]+(X-A[l-1])*(2*l-N))