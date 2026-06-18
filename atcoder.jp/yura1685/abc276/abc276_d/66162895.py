from math import gcd

def f(n):
    yura = 0
    while n % 2 == 0:
        n //= 2
        yura += 1
    while n % 3 == 0:
        n //= 3
        yura += 1
    if n == 1:
        return yura
    else:
        return -1

N = int(input())
A = list(map(int,input().split()))
g = gcd(*A)

ans = 0
for a in A:
    hoge = a//g
    if f(hoge) == -1:
        print(-1)
        exit()
    ans += f(hoge)

print(ans)