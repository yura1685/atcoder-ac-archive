x1, y1, r = map(int,input().split())
x2, y2, x3, y3 = map(int,input().split())

if x1+r <= x3 and x2 <= x1-r and y2 <= y1-r and y1+r <= y3:
    print('NO')
else:
    print('YES')

def dis(x,y):
    return ((x-x1)**2 + (y-y1)**2 <= r**2)

if dis(x2,y2) and dis(x2,y3) and dis(x3,y2) and dis(x3,y3):
    print('NO')
else:
    print('YES')