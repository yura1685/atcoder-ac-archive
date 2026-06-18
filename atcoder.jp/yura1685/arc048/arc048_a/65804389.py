from numpy import sign
A, B = map(int,input().split())
if sign(A) == sign(B):
    print(B-A)
else:
    print(B-A-1)