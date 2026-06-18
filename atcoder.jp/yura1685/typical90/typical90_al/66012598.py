from math import lcm

A, B = map(int,input().split())
L = lcm(A,B)
print('Large' if L > 10**18 else L)