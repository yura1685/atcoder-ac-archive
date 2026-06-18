N = int(input())
D = list(map(int,input().split()))

zoro = 0
for month in range(1,N+1):
    for days in range(1,D[month-1]+1):
        if len(set(str(month)+str(days))) == 1:
            zoro += 1
print(zoro)