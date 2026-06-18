N = int(input())
A = list(map(int,input().split()))

B = [0]*(N+1)
for n in range(N,0,-1):
    cnt = 0
    for i in range(2*n,N+1,n):
        cnt += B[i]
    if cnt % 2 != A[n-1]:
        B[n] = 1

print(sum(B))
for i in range(1,N+1):
    if B[i] > 0:
        print(i,end=' ')