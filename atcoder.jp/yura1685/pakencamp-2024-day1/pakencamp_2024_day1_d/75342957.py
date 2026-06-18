from math import gcd
_, S, T = map(int, input().split())
print(1 if gcd(S, T) < 2 else 2)