W, H = map(int,input().split())

W, H = W-1, H-1
mod = 10**9 + 7

def f(n):
    ans = 1
    for i in range(1,n+1):
        ans = (ans*i) % mod
    return ans

bunsi = f(W+H) % mod
bunbo = (f(W)*f(H)) % mod
inv = pow(bunbo,mod-2,mod)

print((bunsi*inv)%mod)