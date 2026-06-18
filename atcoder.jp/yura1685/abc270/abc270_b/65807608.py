x,y,z = map(int,input().split())
if 0 < x < y or y < x < 0 or y < 0 < x or x < 0 < y:
    print(abs(x))
elif (0 < y < x and z < y) or (x < y < 0 and y < z):
    print(abs(z) + abs(x-z))
else:
    print(-1)