N = int(input())
X = list(map(int,input().split()))
L = sorted(X)
print(sum(L[N:4*N])/(3*N))