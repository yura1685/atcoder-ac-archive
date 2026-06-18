from math import gcd

N = int(input())
A = list(map(int,input().split()))
B = [A[i+1]-A[i] for i in range(N-1)]
g = gcd(*B)
if g == 1:
    print(2)
else:
    print(1)