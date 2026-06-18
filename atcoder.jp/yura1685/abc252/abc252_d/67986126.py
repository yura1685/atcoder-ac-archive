N = int(input())
A = list(map(int,input().split()))
M = max(A)
X = [0]*(M+1)
for a in A:
    X[a] += 1
Y = [x for x in X if x]

x1, x2, x3 = 0, 0, 0
for y in Y:
    x1 += y 
    x2 += y*y 
    x3 += y*y*y

print((x1**3-3*x1*x2+2*x3)//6)