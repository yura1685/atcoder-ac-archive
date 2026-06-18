import bisect

N = int(input())
A = list(map(int,input().split()))
A.sort()

color = 0
for i in range(8):
    n = bisect.bisect_left(A,400*(i+1)) - bisect.bisect_left(A,400*i) 
    if n >= 1:
        color += 1

free = N - bisect.bisect_left(A,3200)
if color == 0:
    print(1,free)
else:
    print(color, color+free)