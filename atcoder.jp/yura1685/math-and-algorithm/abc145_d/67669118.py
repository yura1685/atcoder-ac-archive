X, Y = map(int,input().split())

mod = 10**9 + 7

def f(n):
    ans = 1
    for i in range(1,n+1):
        ans = (ans*i) % mod
    return ans

if (X+Y) % 3 == 0:
    n = (X+Y) // 3
    X, Y = X-n, Y-n
else:
    print(0); exit()
if X < 0 or Y < 0:
    print(0); exit()

bunsi = f(X+Y)
bunbo = (f(X)*f(Y)) % mod
bun = pow(bunbo,mod-2,mod)

print((bunsi*bun)%mod)