n = int(input())
point = []
for i in range(n):
    point.append(list(map(int,input().split())))

d = 0
for i in range(n):
    for j in range(i+1,n):
        d = max(d,(point[i][0]-point[j][0])**2+(point[i][1]-point[j][1])**2)
print(d**(1/2))