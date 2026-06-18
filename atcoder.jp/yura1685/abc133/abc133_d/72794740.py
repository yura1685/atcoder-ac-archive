N = int(input())
A = list(map(int,input().split()))
S = sum(A)
B = [-1] * N

b1 = S - 2*sum(A[1::2])
B[0] = b1

for i in range(1,N):
    B[i] = 2*A[i-1] - B[i-1]

print(*B)