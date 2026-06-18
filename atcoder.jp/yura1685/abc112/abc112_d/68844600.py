from math import isqrt

N, M = map(int,input().split())

res = []
rM = isqrt(M)
for i in range(1,isqrt(M)+1):
    if M % i == 0:
        res.append(i)
        if i**2 != M:
            res.append(M//i)

res.sort(reverse=True)

ans = 1
for g in res:
    if g * N <= M: exit(print(g))