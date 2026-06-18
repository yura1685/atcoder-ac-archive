N = int(input())
A = list(map(int,input().split()))
A.sort()

B = A[:(N+1)//2]
C = A[(N+1)//2:]

for i in range(N//2):
    if not (B[i] < C[i] and B[i+1] < C[i]):
        print('No')
        exit()
print('Yes')