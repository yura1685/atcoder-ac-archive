from math import isqrt

N = int(input())
ans = []
rN = isqrt(N)
for i in range(1,isqrt(N)+1):
    if N % i == 0:
        ans.append(i)
        if i**2 != N:
            ans.append(N//i)

ans.sort()
for i in ans:
    print(i)