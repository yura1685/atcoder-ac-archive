from fractions import Fraction

A, B, C, D, E, F = map(int, input().split())

M = Fraction(0, 1)
ans = (100*A, 0)

water, sugar = set(), set()
for a in range(101):
    for b in range(101):
        w = 100 * (A*a + B*b)
        if 0 < w <= F:
            water.add(w)

for c in range(3001):
    for d in range(3001):
        s = C*c + D*d 
        if s <= F:
            sugar.add(s)

for w in water:
    for s in sugar:
        if w + s > F or w // 100 * E < s:
            continue
        noudo = Fraction(100*s, w + s)
        if noudo > M:
            M = noudo
            ans = (w + s, s)

print(*ans)