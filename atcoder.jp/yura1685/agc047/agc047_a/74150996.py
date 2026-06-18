from fractions import Fraction
inf = 10 ** 9

N = int(input())
A = []
for _ in range(N):
    a = Fraction(input())
    a = a.numerator * (inf // a.denominator)
    c2, c5 = 0, 0
    while a % 2 == 0:
        a //= 2
        c2 += 1
    while a % 5 == 0:
        a //= 5
        c5 += 1
    A.append((min(18,c2), min(18,c5)))

cnt = [[0] * 19 for _ in range(19)]
ans = 0
for c2, c5 in A:
    for x in range(18 - c2, 19):
        for y in range(18 - c5, 19):
            ans += cnt[x][y]
    cnt[c2][c5] += 1
    
print(ans)