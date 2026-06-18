N = int(input())
A = list(map(int,input().split()))
A = [0] + A + [0]
c = [0]*(N+2)

E = 0
for i in range(1,N+1):
    E += abs(A[i]-A[i-1])
    c[i] = abs(A[i]-A[i-1]) + abs(A[i+1]-A[i]) - abs(A[i+1]-A[i-1])
E += abs(A[N])
for i in range(1,N+1):
    print(E-c[i]) 
