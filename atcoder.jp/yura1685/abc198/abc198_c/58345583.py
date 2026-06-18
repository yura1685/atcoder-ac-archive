R, X, Y = map(int,input().split())
way = (X**2+Y**2)**(1/2)
warp = 0
if way % R == 0:
    print(int((way//R)))
    exit()
if R < way:
    print(int(way//R)+1)
else:
    print(2)