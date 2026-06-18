from math import lcm

N, A, B = map(int,input().split())

def f(n):
    c = N // n
    return n*c*(c+1)//2

print(f(1)-f(A)-f(B)+f(lcm(A,B)))