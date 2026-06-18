import math
x = int(input())
n = max(180 - x,x)
u = math.gcd(360,n)
if x == 60:
    print(6)
else:
    print(360//u)