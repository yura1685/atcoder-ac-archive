N, x = map(int,input().split())
A = list(map(int,input().split()))

eat = 0
for i in range(N-1):
    n = max(A[i]+A[i+1]-x, 0)
    A[i+1] -= n
    eat += n
    if i == 0 and A[1] < 0:
        A[1] = 0

print(eat)