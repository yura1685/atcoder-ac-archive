from itertools import product

X = tuple(int(d) for d in input())
A,B,C,D = X

def f(x,y,n):
    if n == 0:
        return x + y
    elif n == 1:
        return x - y

def g(n):
    if n == 0:
        return '+'
    elif n == 1:
        return '-'

c = product([0, 1], repeat=3)
for tup in c:
    ans = A
    ans = f(ans,B,tup[0])
    ans = f(ans,C,tup[1])
    ans = f(ans,D,tup[2])
    if ans == 7:
        print(str(A)+g(tup[0])+str(B)+g(tup[1])+str(C)+g(tup[2])+str(D)+'=7')
        exit()