p = [0,300000,200000,100000]+[0]*202
x, y = map(int,input().split())
print(p[x]+p[y]+400000*(x==y==1))