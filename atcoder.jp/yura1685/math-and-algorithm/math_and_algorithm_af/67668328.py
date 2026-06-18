N = int(input())
point = [tuple(map(int,input().split())) for _ in range(N)]

def dis(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2

ans = float('INF')
for i in range(N-1):
    for j in range(i+1,N):
        xi, yi = point[i]
        xj, yj = point[j]
        ans = min(ans,dis(xi,yi,xj,yj))

print(ans**(1/2))