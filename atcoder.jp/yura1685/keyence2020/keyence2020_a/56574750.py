H = int(input())
W = int(input())
N = int(input())
a = max(H,W)
paint_time = 0
while paint_time*a < N:
    paint_time += 1
print(paint_time)