N = int(input())
nx, ny = 0, 0
cost = 0
for i in range(N):
    x,y=map(int,input().split())
    cost += ((x-nx)**2+(y-ny)**2)**(1/2)
    nx,ny=x,y
cost += (nx**2+ny**2)**(1/2)
print(cost)