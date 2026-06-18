from math import isqrt

N = int(input())

s = set([N])
for d in range(1,isqrt(N-1)+1):
    if (N-1) % d == 0:
        s.add(d)
        s.add((N-1)//d)

for d in range(2,isqrt(N)+1):
    if N % d == 0:
        M = N
        while M % d == 0:
            M //= d
        if (M-1) % d == 0:
            s.add(d)

print(len(s)-1)