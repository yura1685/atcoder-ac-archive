from math import isqrt
def A006218(n):
    res = 0
    rn = isqrt(n)
    for k in range(1,rn+1):
        res += n//k
    return 2*res - rn**2

N = int(input())
print(A006218(N))