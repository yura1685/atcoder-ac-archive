def f(n: int):
    x = list(str(n))
    y = list(reversed(x))
    return x == y

A, B = map(int,input().split())
ans = 0

for X in range(A,B+1):
    ans += f(X)
print(ans)