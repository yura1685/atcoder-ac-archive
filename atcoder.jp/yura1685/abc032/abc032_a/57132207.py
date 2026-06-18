import math

lcm = math.lcm(int(input()),int(input()))
n = int(input())
print((n//lcm)*lcm + lcm if n % lcm != 0 else (n//lcm)*lcm)