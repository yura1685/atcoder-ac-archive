X, Y = map(int,input().split())

n = 1
while X*2**(n-1) <= Y:
    n += 1
print(n-1)