N, K = map(int,input().split())
mod = 1777777777

def stir(X):
    res = 0
    t = 1
    for k in range(X,1,-1):
        res += t*(-1)**k
        res %= mod
        t = (t*k)%mod
    return res

def comb(n,k):
    up, down = 1, 1
    for i in range(k):
        up *= n-i
        down *= i+1
        up, down = up % mod, down % mod
    return up * pow(down,mod-2,mod) % mod

print(comb(N,K)*stir(K)%mod)