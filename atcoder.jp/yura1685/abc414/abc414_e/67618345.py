from sympy import integer_nthroot

N = int(input())
mod = 998244353

def A006218(n):
    return (2*sum(n//k for k in range(1,integer_nthroot(n,2)[0]+1)) 
            - integer_nthroot(n,2)[0]**2)

ans = N*(N+1)//2 - A006218(N)

print(ans % mod)