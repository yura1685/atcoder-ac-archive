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
    
    def comb(self, N: int, r: int) -> int:
        if N > self.size: return 0
        if r < 0 or N < r: return 0
        return (self.fact[N] * self.revFact[N - r] * self.revFact[r]) % self.mod

mod = 10**9 + 7
N, M, K = map(int, input().split())
C = Combination(N*M, mod)
ans = 0
for i in range(N):
    for j in range(M):
        tmp = (N - i) * (M - j) * (i + j)
        if i and j:
            tmp *= 2
        ans += tmp
ans %= mod
print(ans * C.comb(N*M-2, K-2) % mod)