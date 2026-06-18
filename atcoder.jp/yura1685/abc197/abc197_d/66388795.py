import math

N = int(input())
x0, y0 = map(int,input().split())
xn, yn = map(int,input().split())

ox, oy = (x0+xn)/2, (y0+yn)/2

rad = 2*math.pi/N

x1 = (x0-ox)*math.cos(rad) - (y0-oy)*math.sin(rad) + ox
y1 = (x0-ox)*math.sin(rad) + (y0-oy)*math.cos(rad) + oy

print(x1, y1)