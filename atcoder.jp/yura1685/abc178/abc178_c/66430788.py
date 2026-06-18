N = int(input())

mod = 10**9 + 7

x = pow(10,N,mod) - 2*pow(9,N,mod) + pow(8,N,mod)
print(x % mod)