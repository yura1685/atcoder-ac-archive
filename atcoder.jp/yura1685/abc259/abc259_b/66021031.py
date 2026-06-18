import math
a, b, d = map(int,input().split())

theta = math.atan2(b, a)
d = math.radians(d)
r = math.sqrt(a**2+b**2)

print(r*math.cos(theta+d), r*math.sin(theta+d))