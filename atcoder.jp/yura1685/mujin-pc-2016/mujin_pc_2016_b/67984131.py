from math import pi

a, b, c = map(int,input().split())
M = a + b + c

if a + b >= c and b + c >= a and c + a >= b:
    m = 0
else:
    m = min(abs(a+b-c),abs(a-b+c),abs(-a+b+c))

print((M**2-m**2)*pi)