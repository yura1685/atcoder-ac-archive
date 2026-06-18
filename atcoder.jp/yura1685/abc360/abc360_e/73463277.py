mod = 998244353
N, K = map(int,input().split())
if N == 1: exit(print(1))
invN = pow(N,-1,mod)
p = 1
for _ in range(K):
    p = ((1 - 2*(N-1)*invN**2)*p + 2*invN**2*(1-p)) % mod

q = (1-p) * pow(N-1,-1,mod) % mod
ans = p + N*(N+1)//2*q - q
print(ans % mod)