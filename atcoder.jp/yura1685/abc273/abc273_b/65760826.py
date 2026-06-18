def f(n,i):
    min_y = n // (10**(i+1)) * 10**(i+1)
    max_y = min_y + 10**(i+1)
    if abs(n-min_y) < abs(n-max_y):
        return min_y
    else:
        return max_y
    
X, K = map(int,input().split())
for i in range(K):
    X = f(X,i)

print(X)