maisu, yen = map(int,input().split())
for x in range(maisu+1):   
    for y in range(maisu-x+1):
        z = maisu - x - y
        if 10000*x + 5000*y + 1000*z == yen:
            print(x,y,z)
            exit()
print(-1,-1,-1)