N=int(input())
mod=10**9+7
print((pow(4,N+1,mod)-1)*pow(3,mod-2,mod)%mod)