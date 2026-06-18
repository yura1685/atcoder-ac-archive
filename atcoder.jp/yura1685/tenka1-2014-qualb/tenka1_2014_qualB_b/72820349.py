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
    

N = int(input())
S = RollingHash(input())
T = []
mod = 10**9 + 7

for _ in range(N):
    t = RollingHash(input())
    T.append((t.n, t.get()))

dp = [0] * (S.n+1)
dp[0] = 1

for i in range(S.n+1):
    if dp[i] == 0:
        continue
    for n, t in T:
        if i + n > S.n:
            continue
        if S.get(i,i+n) == t:
            dp[i+n] += dp[i]
            dp[i+n] %= mod

print(dp[-1])