import math

A, B, H, M = map(int,input().split())

time = 60*H + M

radH = math.radians(time/2)
radM = math.radians((time % 60)*6)

dis = A*A + B*B -2*A*B*math.cos(radH-radM)
print(math.sqrt(dis))