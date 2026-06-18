K, X = map(int,input().split())
w = []
for i in range(2*K-1):
    w.append(X-K+1+i)
print(*w)