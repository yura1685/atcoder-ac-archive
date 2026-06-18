N, X = map(int,input().split())
A = list(map(int,input().split()))
L = []
for i in range(N):
    if A[i] != X:
        L.append(A[i])
print(*L)