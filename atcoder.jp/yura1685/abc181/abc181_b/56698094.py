def f(x,y):
    return (x+y)*(-x+y+1)//2

ans = 0
n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    ans += f(a,b)

print(ans)