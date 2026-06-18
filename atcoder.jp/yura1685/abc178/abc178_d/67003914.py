S = int(input())
mod = 10**9 + 7

def f(n):
    fact = 1
    for i in range(1,n+1):
        fact = (fact*i) % mod
    return fact

ans = 0
for n in range(1,S//3+1):
    N = S - 3*n
    # 長さn，非負整数からなる数列で総和がNと言い換えられた
    # これは、N個の◯と(n-1)個の|の並び替えに等しい
    # つまりこれはbin((N+n-1),n-1)=f(N+n-1)/(f(N)f(n-1))
    bunsi = f(N+n-1)
    bunbo = (f(N)*f(n-1)) % mod
    ans += (bunsi*pow(bunbo,mod-2,mod)) % mod
    ans %= mod

print(ans)