N = int(input())
A = list(map(int,input().split()))

In = 0
Out = 0
for i in range(N-1):
    if A[i+1] - A[i] > 0:
        In += A[i+1] - A[i]
    else:
        Out += -A[i+1] + A[i]

print(In, Out)