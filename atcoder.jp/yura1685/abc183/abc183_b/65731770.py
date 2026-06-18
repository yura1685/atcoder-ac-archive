Sx, Sy, Gx, Gy = map(int,input().split())

if Sx == Gx:
    print(Sx)
else:
    print((Sy*Gx+Sx*Gy)/(Sy+Gy))