N, K, X = map(int,input().split())
A = list(map(int,input().split()))
i = 0
while True:
    if i == N or K == 0:
        break
    if A[i] >= X:
        c = A[i] // X
        A[i] -= X*min(K, c)
        K -= min(K, c)
    if A[i] < X:
        i += 1
A = sorted(A, reverse = True)        

if K > N:
    print(0)
else:
    print(sum(A[K:]))