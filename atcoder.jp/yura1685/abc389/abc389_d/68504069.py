from math import isqrt

R = int(input())
R = 2*R

ans = (isqrt(R*R - 1) - 1) // 2
for i in range(3,R+1,2):
    Y = isqrt(R*R - i*i)
    ans += (Y-1)//2
ans = 4*ans + 1

print(ans)