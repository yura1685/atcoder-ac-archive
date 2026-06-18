N = int(input())
P = []
for _ in range(N):
    x, y = map(int,input().split())
    P.append((x,y))

def min(x,y):
    xu, xd = x
    yu, yd = y
    if xu*yd < yu*xd:
        return x 
    else:
        return y

def check(X,Y,R2):
    xu, xd = X
    yu, yd = Y
    ru, rd = R2
    for x, y in P:
        if ((xu-x*xd)**2*yd**2 + (yu-y*yd)**2*xd**2)*rd > ru*xd**2*yd**2:
            return False
    return True

def circumcente1(p1,p2,p3):
    (x1, y1), (x2, y2), (x3, y3)  = p1, p2, p3
    xu, xd = (x1**2*y2 - x1**2*y3 - x2**2*y1 + x2**2*y3 + x3**2*y1 - x3**2*y2 + y1**2*y2 - y1**2*y3 - y1*y2**2 + y1*y3**2 + y2**2*y3 - y2*y3**2, 2*x1*y2 - 2*x1*y3 - 2*x2*y1 + 2*x2*y3 + 2*x3*y1 - 2*x3*y2)
    yu, yd = (-x1**2*x2 + x1**2*x3 + x1*x2**2 - x1*x3**2 + x1*y2**2 - x1*y3**2 - x2**2*x3 + x2*x3**2 - x2*y1**2 + x2*y3**2 + x3*y1**2 - x3*y2**2, 2*x1*y2 - 2*x1*y3 - 2*x2*y1 + 2*x2*y3 + 2*x3*y1 - 2*x3*y2)
    R2 = ((x1*xd-xu)**2*yd**2 + (y1*yd-yu)**2*xd**2, xd**2*yd**2)
    if R2[1] == 0:
        return ((0,1),(0,1),(10**8,1))
    else:
        return ((xu,xd),(yu,yd),R2)

ans = (10**8, 1)
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            X, Y, R2 = circumcente1(P[i],P[j],P[k])
            if check(X,Y,R2):
                ans = min(ans, R2)

for i in range(N-1):
    for j in range(i+1,N):
        x1, y1 = P[i]
        x2, y2 = P[j]
        X, Y = (x1+x2,2), (y1+y2,2)
        R2 = ((x1-x2)**2 + (y1-y2)**2, 4)
        if check(X,Y,R2):
            ans = min(ans, R2)

print((ans[0]/ans[1])**(1/2))