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
H, W, A, B = map(int, input().split())
C = Combination(H+W, mod)
M = min(A, B)
ans = C.comb(H+W-2, H-1)
for i in range(M):
    h, w = H-A+i, B-1-i
    ans -= C.comb(h+w, h) * C.comb(H+W-h-w-2, H-h-1)
    ans %= mod

print(ans)