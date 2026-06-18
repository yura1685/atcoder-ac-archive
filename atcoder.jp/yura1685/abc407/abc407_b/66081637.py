X, Y = map(int,input().split())

p = 0
for i in range(1,7):
    for j in range(1,7):
        if (i+j) < X and abs(i-j) < Y:
            p += 1

print(1-(p/36))