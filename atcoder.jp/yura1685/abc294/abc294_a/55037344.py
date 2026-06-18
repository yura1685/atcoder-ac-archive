N = int(input())
A = list(map(int,input().split()))
L = []
for i in range(N):
    if A[i] % 2 == 0:
        L.append(A[i])
print(*L)