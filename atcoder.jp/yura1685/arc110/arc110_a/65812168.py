from math import lcm

N = int(input())
x = 1
for i in range(1,N+1):
    x = lcm(x,i)
print(x+1)