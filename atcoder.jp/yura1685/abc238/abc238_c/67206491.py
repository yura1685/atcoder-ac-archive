mod = 998244353
N = int(input())
ans = (N+1)*(N+2)//2
ans %= mod
L = len(str(N))
for i in range(1,L):
    ans -= 9*100**(i-1)
    ans %= mod
ans -= (N-10**(L-1)+1)*10**(L-1)+1
print(ans%mod)