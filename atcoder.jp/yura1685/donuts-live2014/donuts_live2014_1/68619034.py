N = int(input())
A = list(map(int,input().split()))

print('error' if N % 2 == 1 else sum(A[2*i+1]-A[2*i] for i in range(N//2)))