from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))
B = []
for a in A:
    d = defaultdict(int)
    p = 2
    while a != 1:
        if p*p > a:
            d[a] += 1
            break        
        if a % p == 0:
            a //= p
            d[p] += 1
        else:
            if p % 6 == 1:
                p += 4
            elif p % 6 == 5:
                p += 2
            else:
                p = [0,0,3,5][p]
    B.append(d)

def lcm(d1,d2):
    d3 = d1.copy()
    for p in d2:
        if d1[p] < d2[p]:
            d3[p] = d2[p]
    return d3

def div(d2):
    n = xxx
    m = 1
    for p in d2:
        m = (m*pow(p,d2[p],mod)) % mod
    return n*pow(m,mod-2,mod)%mod

mod = 10**9 + 7

LCM = defaultdict(int)
for b in B:
    LCM = lcm(LCM,b)

xxx = 1
for p in LCM:
    xxx = (xxx*pow(p,LCM[p],mod)) % mod

ans = 0
for b in B:
    ans = (ans + div(b)) % mod

print(ans)