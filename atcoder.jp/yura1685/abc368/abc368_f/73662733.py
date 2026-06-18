def f(x):
    x = int(x)
    res = 0
    p = 2
    while x > 1:
        while x % p == 0:
            x //= p
            res += 1
        if x == 1:
            break
        p += 1
        if p * p > x:
            res += 1
            break
    return res

N = int(input())
A = list(map(f ,input().split()))

xor = 0
for a in A:
    xor ^= a 

print('Anna' if xor else 'Bruno')