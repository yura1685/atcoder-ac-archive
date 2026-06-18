from math import isqrt

D = int(input())
ans = 10**10


for x in range(isqrt(D)+2):
    y1 = isqrt(abs(D-x*x))
    y2 = y1+1
    dis = min(abs(x*x+y1*y1-D),abs(x*x+y2*y2-D))
    ans = min(ans, dis)

print(ans)