R, C = map(int,input().split())
A = ['']*2
for i in range(2):
    A[i] = list(map(int,input().split()))
print(A[R-1][C-1])