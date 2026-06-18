from math import ceil, lcm

A, B, C, D = map(int,input().split())

def f(x):
    return B//x - ((A+x-1)//x) + 1

n = f(C) + f(D) - f(lcm(C,D))

print(B-A+1-n)
