N, K, M = map(int,input().split())

mod = 998244353
x = pow(K,N,mod-1) + mod - 1
print(pow(M % mod,x,mod))