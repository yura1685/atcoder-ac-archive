N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
A = sorted(A,reverse = True)
c = 0
for i in range(N):
    if i % 2 == 0:
        c += A[i]**2
    else:
        c -= A[i]**2
print(c*3.14159265358979)