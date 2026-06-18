N, K = map(int, input().split())
L, A = [], []
for _ in range(N):
    l, *a = map(int, input().split())
    L.append(l)
    A.append(a)
C = list(map(int, input().split()))

for i in range(N):
    if L[i] * C[i] < K:
        K -= L[i] * C[i]
    else:
        K = (K - 1) % L[i]
        print(A[i][K])
        break