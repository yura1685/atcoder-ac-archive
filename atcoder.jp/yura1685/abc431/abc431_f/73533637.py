from atcoder.fenwicktree import FenwickTree
from more_itertools import run_length

class Combination:
    def __init__(self, size: int, mod: int):
        self.size = size
        self.mod = mod
        self.fact = [1] * (size + 1)
        for i in range(1, size + 1):
            self.fact[i] = (self.fact[i-1] * i) % mod
        self.factN = self.fact[size]
        self.revFact = [1] * (size + 1)
        self.revFact[size] = pow(self.factN, -1, mod)
        for i in reversed(range(1, size)):
            self.revFact[i] = (self.revFact[i+1] * (i + 1)) % mod

    def combNR(self, N: int, r: int) -> int:
        if N > self.size: return 0
        if r < 0 or N < r: return 0
        return (self.fact[N] * self.revFact[N - r] * self.revFact[r]) % self.mod

mod = 998244353    
N, D = map(int,input().split())
A = sorted(map(int,input().split()))
M = max(A)
ft = FenwickTree(M+1)
C = Combination(N+1, mod)

ans = 1
for a, num in run_length.encode(A):
    cnt = ft.sum(max(0,a-D), M+1)
    ans *= C.combNR(cnt+num, num)
    ans %= mod
    ft.add(a, num)

print(ans)