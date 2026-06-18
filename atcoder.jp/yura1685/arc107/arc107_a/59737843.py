a, b, c = map(int,input().split())
mod = 998244353
A = (a*(a+1)//2) % mod
B = (b*(b+1)//2) % mod
C = (c*(c+1)//2) % mod

print((A*B*C) % mod)