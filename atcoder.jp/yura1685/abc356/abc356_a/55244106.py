N, L, R = map(int, input(). split())
A = []
for i in range(N):
    A.append(i+1)
for i in range(R-L+1):
    A[L+i-1] = R - i
print(*A)