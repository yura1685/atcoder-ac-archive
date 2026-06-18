N, K = map(int,input().split())
A = list(map(int,input().split()))

INF = float('inf')

X = []
for i in range(K):
    X.append(sorted(A[i:N:K]))

Y = []
for i in range(N):
    a, b = divmod(i,K)
    Y.append(X[b][a])

if Y == sorted(Y):
    print('Yes')
else:
    print('No')