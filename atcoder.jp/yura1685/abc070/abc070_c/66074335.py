from math import lcm
N = int(input())
t = 1
for _ in range(N):
    T = int(input())
    t = lcm(t,T)

print(t)