N = int(input())
A = ['']*N
for i in range(N):
    A[i] = list(map(int,input().split()))
for j in range(N):
    L = []
    for k in range(N):
        if A[k][j] == 1:
            L.append(k+1)
    M = []
    for l in range(len(L)):
        M.append(str(L[l]))
    print(*M)