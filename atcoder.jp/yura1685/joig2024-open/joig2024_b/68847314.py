N, D = map(int,input().split())
A = sorted(map(int,input().split()))

for i in range(N):
    a, b = A[2*i], A[2*i+1]
    if b > a + D:
        exit(print('No'))
print('Yes')