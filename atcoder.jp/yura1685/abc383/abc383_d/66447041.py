from sympy.ntheory.generate import sieve, primerange

N = int(input())

P = list(sieve.primerange(2,int(N**(1/2))+1))
n = len(P)

ans = 0
for p in P:
    if p**8 <= N:
        ans += 1
    else:
        break

for x in range(n):
    p = P[x]
    if p*p*p*p > N:
        break
    for y in range(x+1,n):
        q = P[y]
        if p*p*q*q <= N:
            ans += 1
        else:
            break

print(ans)