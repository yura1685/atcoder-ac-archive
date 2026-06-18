from collections import defaultdict

def isqrt(n):
    ok, ng = 0, n+1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if mid ** 2 > n:
            ng = mid
        else:
            ok = mid
    return ok

class Sieve_of_Eratosthenes:
    def __init__(self, n: int) -> None:
        self.n:list[bool] = [False, False] + [True] * (n - 1)
        self.primes:list[int] = []
        for i in range(2,n+1):
            if not self.n[i]: continue
            self.primes.append(i)
            for j in range(2*i,n+1,i):
                self.n[j] = False
    
    def is_prime(self, p: int) -> bool:
        return self.n[p]
    
N = int(input())
S = [int(input()) for _ in range(N)]
M = max(S)

SoE = Sieve_of_Eratosthenes(isqrt(M))
Primes = SoE.primes

D = defaultdict(list)
Mod3  = [0] * N
Pairs = [0] * N

for i, s in enumerate(S):
    p = defaultdict(int)
    for prime in Primes:
        while s % prime == 0:
            s //= prime
            p[prime] += 1
        if s == 1:
            break
        if prime * prime >= s:
            p[s] += 1
            break
    else:
        if s > 1: p[s] += 1
    n = 1
    pair = 1
    for prime, cnt in p.items():
        cnt %= 3
        if cnt:
            n *= prime ** cnt
            pair *= prime ** (3-cnt)
    D[n].append(i)
    Mod3[i] = n
    Pairs[i] = pair

check = set()
ans = 0

for i in range(N):
    n = Mod3[i]
    pair = Pairs[i]
    if n in check:
        continue
    check.add(n)
    check.add(pair)
    if n == 1:
        ans += 1
    else:
        ans += max(len(D[n]), len(D[pair]))

print(ans)