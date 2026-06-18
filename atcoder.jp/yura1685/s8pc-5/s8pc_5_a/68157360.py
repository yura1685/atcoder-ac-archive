N, T = map(int,input().split())
A = list(map(int,input().split()))

for i in range(1,N):
    if A[i-1] > A[i]:
        k = (A[i-1] - A[i] + T - 1)//T
        A[i] += k*T

print(A[-1])