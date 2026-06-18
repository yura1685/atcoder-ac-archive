from bisect import bisect, bisect_left
m = int(input())

want = [(0,0)]
a, b = map(int,input().split())
for _ in range(m-1):
    c, d = map(int,input().split())
    want.append((c-a,d-b))

n = int(input())
sky = [tuple(map(int,input().split())) for _ in range(n)]
sky.sort()

for x, y in sky:
    for dx, dy in want:
        s, t = x+dx, y+dy
        if bisect(sky,(s,t)) == bisect_left(sky,(s,t)):
            break
    else:
        print(x-a,y-b)
        exit()