from math import isqrt

class Sieve_of_Eratosthenes:
    def __init__(self, n: int) -> None:
        self.n = [False, False] + [True] * (n - 1)
        self.prime = []
        for i in range(2,n+1):
            if not self.n[i]: continue
            self.prime.append(i)
            for j in range(2*i,n+1,i):
                self.n[j] = False
    
    def is_prime(self, p: int) -> bool:
        return self.n[p]

L, R = map(int,input().split())
SoE = Sieve_of_Eratosthenes(isqrt(R))
P = SoE.prime

ans = 0
furui = [0] * (R-L+1)

for p in P:
    l = max(L + (-L) % p, p)
    for n in range(l,R+1,p):
        N = n
        if furui[N-L] == -1:
            continue
        while n % p == 0:
            n //= p 
        if n == 1:
            furui[N-L] = 1
        else:
            furui[N-L] = -1

ans = furui.count(0) + furui.count(1) + (furui[0] == -1)
print(ans)