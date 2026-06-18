N = int(input())
A = list(map(int,input().split()))

M = 0
S = 0
T = 0
for i in range(1,N+1):
    M = max(M, A[i-1])
    T += A[i-1]
    S += T
    print(S+i*M)
