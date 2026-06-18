def f(X):return X//4-X//100+X//400
A,B=map(int,input().split())
print(f(B)-f(A-1))