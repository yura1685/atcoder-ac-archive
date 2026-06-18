class RollingHash:
    def __init__(self, s, base=1007, mod=998244353):
        self.mod = mod
        self.n = len(s)
        self.base = base
        self.hash = [0] * (self.n + 1)
        self.pow = [1] * (self.n + 1)
        
        for i in range(self.n):
            self.hash[i + 1] = (self.hash[i] * self.base + ord(s[i])) % self.mod
            self.pow[i + 1] = (self.pow[i] * self.base) % self.mod

    def get(self, l=0, r=None):
        """
        S[l:r] のハッシュ値を取得．
        """
        if r is None:
            r = self.n

        res = self.hash[r] - self.hash[l] * self.pow[r - l]
        return res % self.mod

    def __len__(self):
        return self.n
    
def solve():
    A = RollingHash(input())
    B = RollingHash(input())
    N = A.n
    for i in range(N):
        if A.get(0,i) == B.get(N-i,N) and A.get(i,N) == B.get(0,N-i):
            print(i)
            return 
    print(-1)

T = int(input())
for _ in range(T):
    solve()