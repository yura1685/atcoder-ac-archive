def intersect(p1, p2, p3, p4):
    def cross_product(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    cp1 = cross_product(p1, p2, p3)
    cp2 = cross_product(p1, p2, p4)
    cp3 = cross_product(p3, p4, p1)
    cp4 = cross_product(p3, p4, p2)
    return (cp1*cp2 < 0) and (cp3*cp4 < 0)

ax, ay, bx, by = map(int,input().split())
N = int(input())
P = []
for _ in range(N):
    x, y = map(int,input().split())
    P.append((x,y))
P.append(P[0])

cnt = 0
p1, p2 = (ax, ay), (bx, by)
for i in range(N):
    p3, p4 = P[i], P[i+1]
    if intersect(p1, p2, p3, p4):
        cnt += 1

print(cnt//2+1)