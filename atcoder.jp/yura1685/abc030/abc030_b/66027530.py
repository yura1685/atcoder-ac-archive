n, m = map(int,input().split())
n %= 12

argm = 6*m
argn = 30*n + 0.5*m

print(min(abs(argm-argn), 360-abs(argm-argn)))