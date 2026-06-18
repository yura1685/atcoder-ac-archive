N = int(input())
C = [0] * 6
mod = 998244353
inv5 = pow(5,-1,mod)

while N % 2 == 0:
    N //= 2
    C[2] += 1
while N % 3 == 0:
    N //= 3
    C[3] += 1
while N % 5 == 0:
    N //= 5
    C[5] += 1

if N > 1: exit(print(0))

P = []
for i in range(min(C[2],C[3])+1):
    L = [0,0,C[2]-i,C[3]-i,0,C[5]]
    for j in range(L[2]//2+1):
        P.append((L[2]-2*j, L[3], j, L[5], i))

fact = [1]
finv = [1]
for i in range(1,100):
    fact.append(fact[-1] * i % mod)
    finv.append(pow(fact[-1],-1,mod))

ans = 0
for p in P:
    X = fact[sum(p)] * finv[p[0]] * finv[p[1]] * finv[p[2]] * finv[p[3]] * finv[p[4]] % mod
    X *= pow(inv5, p[0], mod) * pow(inv5, p[1], mod) * pow(inv5, p[2], mod) * pow(inv5, p[3], mod) * pow(inv5, p[4], mod)
    ans += X % mod

print(ans % mod)