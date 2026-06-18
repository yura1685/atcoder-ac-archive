N = int(input())
n = len(str(N))
mod = 998244353
u = N*(pow(pow(10,n,mod),N,mod)-1)
d = pow(pow(10,n,mod)-1,mod-2,mod)
print((u*d)%mod)