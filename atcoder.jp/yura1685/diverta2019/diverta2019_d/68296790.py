from math import isqrt

N = int(input())
ans = set()

for c in range(1,isqrt(N)+1):
    if N % c == 0:
        m = N//c - 1
        if m and N % m == N // m:
            ans.add(m)
        m = N//(N//c) - 1
        if m and N % m == N // m:
            ans.add(m)

print(sum(ans))