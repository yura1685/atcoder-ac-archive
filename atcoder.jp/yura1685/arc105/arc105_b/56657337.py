import math
import functools

N = int(input())
d = list(map(int,input().split()))
print(functools.reduce(math.gcd,d))