N = int(input())
A = list(map(int,input().split()))
from math import lcm
print(lcm(*A))