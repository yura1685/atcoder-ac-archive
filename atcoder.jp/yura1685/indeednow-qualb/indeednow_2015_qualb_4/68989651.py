N, C = map(int,input().split())
A = list(map(int,input().split()))
cnt = [[0] for _ in range(C+1)]

for i in range(N):
    if A[i] <= C:
        cnt[A[i]].append(i+1)

M = N*(N+1)//2
for i in range(1,C+1):
    L = cnt[i]
    L.append(N+1)
    res = 0
    for j in range(len(L)-1):
        w = L[j+1] - L[j] - 1
        res += w*(w+1)//2
    print(M - res)