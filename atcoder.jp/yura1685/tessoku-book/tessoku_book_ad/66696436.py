def gyakugen(n, p): # 1/n mod p
    return pow(n,p-2,p) % p

def f(n,p): # n! mod p
    ans = 1
    for i in range(1,n+1):
        ans *= i
        ans %= p
    return ans

n, r = map(int, input().split())
p = 1000000007

bunsi = f(n,p)
bunbo = f(r,p)*f(n-r,p) % p

print(bunsi*gyakugen(bunbo,p) % p )