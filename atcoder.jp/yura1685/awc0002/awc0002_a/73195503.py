N, K = map(int,input().split())
A = list(map(int,input().split()))
print(A.index(K)+1 if K in A else -1)