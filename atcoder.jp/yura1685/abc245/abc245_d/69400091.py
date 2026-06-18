N, M = map(int,input().split())
A = list(map(int,input().split()))[::-1]
C = list(map(int,input().split()))[::-1]
B = []

for i in range(M + 1):
    r = C[i] // A[0]
    B.append(r)
    for j in range(N + 1):
        C[i+j] -= r*A[j]

print(*B[::-1])