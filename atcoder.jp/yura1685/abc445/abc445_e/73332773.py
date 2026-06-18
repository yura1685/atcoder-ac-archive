from collections import defaultdict

class Sieve_of_Eratosthenes:
    def __init__(self, n: int) -> None:
        self.n = [False, False] + [True] * (n - 1)
        for i in range(2,n+1):
            if not self.n[i]: continue
            for j in range(2*i,n+1,i):
                self.n[j] = False
    
    def is_prime(self, p: int) -> bool:
        return self.n[p]

def f(L: list, n: int) -> None:
    if n > L[0]:
        L[1] = L[0]
        L[0] = n
    elif n > L[1]:
        L[1] = n

SoE = Sieve_of_Eratosthenes(3200)
P = [p for p in range(1,3200) if SoE.is_prime(p)]
mod = 998244353

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    D = [defaultdict(int) for _ in range(N)]

    for i, a in enumerate(A):
        for p in P:
            if p * p > a: break
            while a % p == 0:
                D[i][p] += 1
                a //= p 
            if a == 1:
                break
        if a > 1:
            D[i][a] += 1

    P_cnt = defaultdict(lambda: [0, 0])
    for i in range(N):
        for p, cnt in D[i].items():
            f(P_cnt[p], cnt)

    LCM = 1
    for p, s in P_cnt.items():
        LCM = (LCM * pow(p,max(s),mod)) % mod
    
    ans = []
    for i in range(N):
        cur = LCM
        for p, e in D[i].items():
            if e == P_cnt[p][0]:
                diff = P_cnt[p][0] - P_cnt[p][1]
                if diff:
                    cur = (cur * pow(pow(p, diff, mod), mod-2, mod)) % mod
        ans.append(cur)
    
    print(*ans)

for _ in range(int(input())):
    solve()