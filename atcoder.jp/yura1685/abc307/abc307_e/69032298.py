N, M = map(int,input().split())
mod = 998244353

print(((-1)**N * (M-1) + pow(M-1,N,mod)) % mod)