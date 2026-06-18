N, K = map(int,input().split())
L = list(map(int,input().split()))
l = sorted(L)
A = []
for i in range(K+1):
    A.append(l[N-K+i-1] - l[i])
print(min(A))