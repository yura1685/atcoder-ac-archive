from bisect import bisect,bisect_left
N=int(input())
A=list(map(int,input().split()))
W=[[]for _ in range(N+1)]
for i in range(N):W[A[i]].append(i+1)
Q=int(input())
for _ in range(Q):L,R,X=map(int,input().split());print(bisect(W[X],R)-bisect_left(W[X],L))