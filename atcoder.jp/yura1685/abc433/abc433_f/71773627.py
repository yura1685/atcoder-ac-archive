from itertools import accumulate

S = input()
N = len(S)
mod = 998244353
cnt = [[0]*N for _ in range(10)]
for i in range(N):
    s = int(S[i])
    cnt[s][i] += 1

ac = [list(accumulate(X)) for X in cnt]

fact = [1]
f = 1
for i in range(1,N+1):
    f = f * i % mod
    fact.append(f)

tcaf = []
for f in fact:
  tcaf.append(pow(f,mod-2,mod))

def comb(n,k):
    if n < k: return 0
    return fact[n] * tcaf[n-k] * tcaf[k] % mod

ans = 0
for i in range(N):
    s = int(S[i])
    if s == 9: continue
    p = ac[s][i] - 1
    q = ac[s+1][-1] - ac[s+1][i]
    ans += comb(p+q,p+1)
    ans %= mod

print(ans)