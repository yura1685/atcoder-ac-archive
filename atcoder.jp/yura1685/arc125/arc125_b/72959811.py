from math import isqrt

N = int(input())
mod = 998244353
ans = 0
for s in range(1,isqrt(N)+1):
    l, r = s, N//s
    ans += (r-l)//2+1
    ans %= mod
    
print(ans % mod)