A, B, C, X, Y = map(int,input().split())

ans = 10**18
for i in range(0,2*max(X,Y)+1,2):
    pay = C*i
    x, y = max(0,X-i//2), max(0,Y-i//2)
    pay += A*x + B*y
    ans = min(ans,pay)

print(ans)