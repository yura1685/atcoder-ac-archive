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

mod = 10 ** 9 + 7    
x1, y1, x2, y2 = map(int, input().split())
C = Combination(x2 + y2 + 10, mod)

def f(x, y): return C.comb(x+1+y, x+1)

ans = 0
for x in range(x1, x2 + 1):
    ans += f(x, y2) - f(x, y1-1)

print(ans % mod)