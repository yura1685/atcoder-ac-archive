from math import comb

S = input()
o, q, x = S.count('o'), S.count('?'), S.count('x')

ans = 0
for i in range(q+1):
    n = o+i
    c = 0
    if n == 1:
        c = 1
    if n == 2:
        c = 14
    if n == 3:
        c = 36
    if n == 4:
        c = 24
    if c == 0:
        continue
    ans += c*comb(q,i)
print(ans)