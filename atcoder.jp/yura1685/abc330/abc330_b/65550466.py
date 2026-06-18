N, L, R = map(int,input().split())
A = list(map(int,input().split()))

for i in range(N):
    A_i = A[i]
    if L <= A_i <= R:
        X = A_i
    elif A_i < L:
        X = L
    else:
        X = R
    print(X,end=' ')