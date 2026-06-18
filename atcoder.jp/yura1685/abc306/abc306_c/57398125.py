N = int(input())
A = list(map(str,input().split()))
c = [0]*(N+1)
L = []

for i in range(3*N):
    c[int(A[i])] += 1
    if c[int(A[i])] == 2:
        L.append(int(A[i]))
print(*L)