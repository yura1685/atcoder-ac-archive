from math import isqrt

N = int(input())
M = N
ans = 1
p = 2
while M != 1:
    cnt = 1
    sigma = 1
    if p*p > N:
        ans *= M+1
        break
    while M % p == 0:
        sigma += p**cnt
        cnt += 1
        M //= p
    ans *= sigma
    p += 1

ans -= N

if ans < N:
    print('Deficient')
if ans == N:
    print('Perfect')
if ans > N:
    print('Abundant')