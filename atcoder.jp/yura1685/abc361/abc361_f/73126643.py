from math import isqrt

N = int(input())
ans = isqrt(N)
s = set()
for p in [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]:
    n = 2
    while 1:
        X = n ** p
        if X > N:
            break
        if isqrt(X) ** 2 != X and X not in s:
            ans += 1
            s.add(X)
        n += 1

print(ans)