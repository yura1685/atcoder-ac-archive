n, a, b = map(int,input().split())
mod = 10**9 + 7

def f(x): # nCxを計算する
    bunsi, bunbo = 1, 1
    for i in range(1,x+1):
        bunbo = (bunbo*i)%mod
        bunsi = (bunsi*(n-i+1))%mod
    return bunsi, bunbo

def flower(x):
    bunsi, bunbo = f(x)
    bunbo = pow(bunbo,mod-2,mod)
    return (bunsi*bunbo)%mod

ans = pow(2,n,mod) - 1 - flower(a) - flower(b)
print(ans % mod)