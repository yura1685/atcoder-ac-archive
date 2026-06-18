from math import gcd

N = int(input())
A = list(map(int,input().split()))
g = gcd(*A)
print(g)