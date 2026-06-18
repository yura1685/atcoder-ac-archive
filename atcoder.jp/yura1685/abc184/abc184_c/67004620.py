r1, c1 = map(int,input().split())
r2, c2 = map(int,input().split())
r2 -= r1
c2 -= c1
if r2 < 0:
    r2 = -r2
if c2 < 0:
    c2 = -c2

x, y = r2, c2

if x == y:
    if x == 0:
        print(0)
    else:
        print(1)
    exit()

if x + y <= 3:
    print(1)
    exit()

if x + y <= 6:
    print(2)
    exit()

if (x + y) % 2 == 0:
    print(2)
    exit()

if abs(x-y) <= 3:
    print(2)
    exit()

print(3)