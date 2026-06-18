from math import isqrt

N = int(input())
A = list(map(int,input().split()))
L = [1] + [0] * (N-1)
B = isqrt(N)
mod = 998244353

small = [[0] * step for step in range(B+1)]

for i in range(N):
    for step in range(1,B+1):
        L[i] += small[step][i % step]
    L[i] %= mod
    
    a = A[i]
    if a > B:
        for n in range(i+a, N, a):
            L[n] += L[i]
    else:
        small[a][i % a] += L[i]
        small[a][i % a] %= mod

print(sum(L) % mod)