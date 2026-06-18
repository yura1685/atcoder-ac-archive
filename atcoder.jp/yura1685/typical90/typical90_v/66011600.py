from math import gcd
a, b, c = map(int,input().split())
x = gcd(a,gcd(b,c))

print(a//x + b//x + c//x - 3)