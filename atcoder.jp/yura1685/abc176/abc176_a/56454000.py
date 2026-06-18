n,x,t=map(int,input().split())
make = 0
while make < n:
    make += x
print(make//x*t)