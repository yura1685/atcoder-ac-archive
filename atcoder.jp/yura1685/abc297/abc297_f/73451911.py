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
    
    def comb(self, r: int) -> int:
        if r < 0 or self.size < r: return 0
        return (self.factN * self.revFact[self.size - r] * self.revFact[r]) % self.mod
    
    def combNR(self, N: int, r: int) -> int:
        if N > self.size: return 0
        if r < 0 or N < r: return 0
        return (self.fact[N] * self.revFact[N - r] * self.revFact[r]) % self.mod

mod = 998244353
H, W, K = map(int,input().split())
C = Combination(H*W, mod)
HWCK = C.comb(K)
ans = 0
for x in range(1,H+1):
    for y in range(1,W+1):
        U = C.combNR((x-1)*W, K)
        R = C.combNR(H*(W-y), K)
        D = C.combNR((H-x)*W, K)
        L = C.combNR(H*(y-1), K)
        UR = C.combNR((x-1)*(W-y), K)
        RD = C.combNR((H-x)*(W-y), K)
        DL = C.combNR((H-x)*(y-1), K)
        LU = C.combNR((x-1)*(y-1), K)
        ans += HWCK - (U + R + D + L) + (UR + RD + DL + LU)
        ans %= mod

print(ans * pow(HWCK, -1, mod) % mod)