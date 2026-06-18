from collections import defaultdict

N = int(input())
d = defaultdict(int)
for n in range(2, N+1):
    for p in range(2, n+1):
        while n % p == 0:
            d[p] += 1
            n //= p

ans = 0
primes = list(d.keys())

if d[2] >= 74: ans += 1

for p1 in primes:
    for p2 in primes:
        if p1 >= p2: continue
        if d[p1] >= 24 and d[p2] >= 2: ans += 1
        if d[p1] >= 2 and d[p2] >= 24: ans += 1
        if d[p1] >= 14 and d[p2] >= 4: ans += 1
        if d[p1] >= 4 and d[p2] >= 14: ans += 1

for p1 in primes:
    for p2 in primes:
        for p3 in primes:
            if not (p1 < p2 < p3): continue
            if d[p1] >= 2 and d[p2] >= 4 and d[p3] >= 4: ans += 1
            if d[p1] >= 4 and d[p2] >= 2 and d[p3] >= 4: ans += 1
            if d[p1] >= 4 and d[p2] >= 4 and d[p3] >= 2: ans += 1

print(ans)