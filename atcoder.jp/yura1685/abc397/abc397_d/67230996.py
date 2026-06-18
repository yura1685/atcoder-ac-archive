from math import isqrt

N = int(input())

for u in range(1,10**18):
    if u*u*u > N:
        break
    if N % u != 0:
        continue
    v = N//u
    v -= u*u
    if v % 3 != 0 or v <= 0:
        continue
    s = u    
    t = v//3 
    y = (-s+isqrt(s*s+4*t))//2
    if y*y + s*y - t == 0:
        print(s+y,y)
        exit()

print(-1)