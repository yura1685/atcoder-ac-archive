N, D = map(int,input().split())
point = []
for i in range(N):
    x, y = map(int,input().split())
    point.append([x,y])

virus = [0]*N
virus[0] = 1

check = [0]

def d(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)

while len(check) != 0:
    for i in range(N):
        if d(point[check[0]],point[i]) <= D:
            if virus[i] == 0:
                virus[i] = 1
                check.append(i)
    check.pop(0)

for i in range(N):
    if virus[i] == 1:
        print('Yes')
    else:
        print('No')