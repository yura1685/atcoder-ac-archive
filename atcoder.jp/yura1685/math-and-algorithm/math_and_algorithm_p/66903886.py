from math import gcd

N = int(input())
A = list(map(int,input().split()))
print(gcd(*A))