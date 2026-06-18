from math import isqrt
from itertools import permutations

S = input()
if len(set(S)) > 5: exit(print(-1))
alp = list(set(S))
N = isqrt(10 ** len(S))
prime = [False, False] + [True] * (N-1)

for p in range(2,N+1):
    if not prime[p]:
        continue
    for i in range(2*p,N+1,p):
        prime[i] = False

d = {}

P = [i for i in range(N+1) if prime[i]]

del N

ans = []
def solve(N):
    if N == 1:
        return 
    for p in P:
        if N % p == 0 and N != p:
            return 
    else:
        exit(print(N))

for X in permutations(['1','3','5','7','9'], len(alp)):
    for i in range(len(alp)): d[alp[i]] = X[i]
    num = [d[q] for q in S]
    solve(int(''.join(num)))

print(-1)