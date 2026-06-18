x, y = map(int,input().split())
N = int(input())

def line(x1,y1,x2,y2):
    for a in range(-200,200):
        for b in range(-200,200):
            if a*x1 + b*y1 == a*x2 + b*y2:
                c = -a*x1 - b*y1
                return a, b, c
            
def dist(a,b,c):
    return abs(a*x + b*y + c)/(a*a + b*b)**(1/2)

point = [tuple(map(int,input().split())) for _ in range(N)]
point.append(point[0])

ans = 10**8
for i in range(N):
    x1,y1 = point[i]
    x2,y2 = point[i+1]
    a, b, c = line(x1,y1,x2,y2)
    ans = min(ans,dist(a,b,c))

print(ans)