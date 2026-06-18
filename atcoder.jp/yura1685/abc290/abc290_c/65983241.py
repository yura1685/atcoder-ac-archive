N, K = map(int,input().split())
A = list(map(int,input().split()))

L = [0]*(K+1)
for a in A:
    if a < K:
        L[a] += 1
if 0 in L:
    print(L.index(0))
else:
    print(K)