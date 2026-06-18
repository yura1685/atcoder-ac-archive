import itertools

N = int(input())
arr = [i+1 for i in range(N)]

route = list(itertools.permutations(arr))

x = [0]
y = [0]
for i in range(N):
    X, Y = map(int,input().split())
    x.append(X)
    y.append(Y)

dis = 0
for R in route:
    for i in range(N-1):
        dis += ((x[R[i+1]]-x[R[i]])**2 + (y[R[i+1]]-y[R[i]])**2)**(0.5)

def f(n):
    if n == 0:
        return 1
    else:
        return n*f(n-1)
    
print(dis/f(N))