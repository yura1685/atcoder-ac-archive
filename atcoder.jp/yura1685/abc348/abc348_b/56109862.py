N = int(input())
point = []
for i in range(N):
    x, y = map(int,input().split())
    point.append([x,y])

def dd(a,b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

for i in range(N):
    distance = 0
    far_point = 0
    for j in range(N):
        if distance < dd(point[i],point[j]):
            distance = dd(point[i],point[j])
            far_point = j + 1
    print(far_point)