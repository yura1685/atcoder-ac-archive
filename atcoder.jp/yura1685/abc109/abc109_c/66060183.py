from math import gcd

N, X = map(int,input().split())
x = list(map(int,input().split()))
y = [abs(a - X) for a in x]
print(gcd(*y))