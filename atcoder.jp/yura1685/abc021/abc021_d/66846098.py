n = int(input())
k = int(input())

mod = 10**9 + 7

def f(n):
    ans = 1
    for i in range(1,n+1):
        ans = (ans*i) % mod
    return ans

bunsi = f(n+k-1)
bunbo = (f(k)*f(n-1)) % mod
bun = pow(bunbo,mod-2,mod)

print((bunsi*bun)%mod)