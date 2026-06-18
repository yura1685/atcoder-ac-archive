S = input()
N = len(S)
A = [0]*N
C = [0]*N
Wl, Wr = [0]*N, [0]*N

for i in range(N):
    s = S[i]
    if s == 'A' and i < N-1:
        A[i+1] = 1
    if s == 'C' and i > 0:
        C[i-1] = 1
    if s == '?' and i < N-1:
        Wl[i+1] = 1
    if s == '?' and i > 0:
        Wr[i-1] = 1

for i in range(N-1):
    A[i+1] += A[i]
    Wl[i+1] += Wl[i]
for i in range(N-2,-1,-1):
    C[i] += C[i+1]
    Wr[i] += Wr[i+1]

mod = 10**9 + 7

def f(n):
    res = 1
    for i in range(1,n+1):
        res = (res*i)%mod
    return res

def comb(n,k):
    bunbo = f(k)
    bunsi = 1
    for i in range(k):
        bunsi = bunsi * (n-i) % mod
    return bunsi * pow(bunbo,mod-2,mod) % mod

def si(a,A):
    return (A + 3*a) * pow(3,A-1,mod) % mod

ans = 0
for z in range(1,N-1):
    s = S[z]
    if s not in 'B?': continue
    a, c = A[z], C[z]
    aa, cc = Wl[z], Wr[z]
    AAA = si(a,aa)
    CCC = si(c,cc)
    ans = (ans + AAA * CCC) % mod

print(ans)