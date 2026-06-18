from collections import defaultdict

N = int(input())
ball = [tuple(map(int,input().split())) for _ in range(N)]
d = defaultdict(int)

if N == 1:
    print(1)
    exit()
    
for i in range(N-1):
    for j in range(i+1,N):
        x1, y1 = ball[i]
        x2, y2 = ball[j]
        x, y = x2-x1, y2-y1
        if x < 0:
            x = -x
            y = -y
        if x == 0:
            if y < 0:
                y = -y
        d[(x,y)] += 1

print(N-max(d.values()))