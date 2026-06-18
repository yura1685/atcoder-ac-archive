N, M = map(int,input().split())

P = []
R = float('inf')

for _ in range(N):
    x, y, r = map(int,input().split())
    R = min(R,r)
    P.append((x,y,r))
for _ in range(M):
    x, y = map(int,input().split())
    P.append((x,y,-1))

def dist(x1,y1,r1,x2,y2,r2):
    if r1 == r2 == -1:
        return ((x1-x2)**2 + (y1-y2)**2)**(1/2)/2
    if r1 == -1:
        return ((x1-x2)**2 + (y1-y2)**2)**(1/2) - r2
    if r2 == -1:
        return ((x1-x2)**2 + (y1-y2)**2)**(1/2) - r1
    return min(r1,r2)

for i in range(N+M-1):
    for j in range(i+1,N+M):
        x1, y1, r1 = P[i]
        x2, y2, r2 = P[j]
        R = min(R,dist(x1,y1,r1,x2,y2,r2))

print(R)