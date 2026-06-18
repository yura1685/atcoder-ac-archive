from math import isqrt

L, R = map(int,input().split())
N = isqrt(R)
prime = [False, False] + [True] * (N-1)

for p in range(2,N+1):
    if not prime[p]:
        continue
    for i in range(2*p,N+1,p):
        prime[i] = False

P = [i for i in range(N+1) if prime[i]]

X = [True] * (R-L+1)
for p in P:
    I = (L+p-1)//p*p - L
    for i in range(I,R-L+1,p):
        if i == p - L:
            continue
        X[i] = False

print(sum(X) - (L==1))
