N = int(input())

def f(x,y):
    return x*x*x+x*x*y+x*y*y+y*y*y

ans = 10**18

for x in range(1000001):
    yl, yr = x, 1000001
    while yl <= yr:
        ym = (yl+yr)//2
        u = f(x,ym)
        if u < N:
            yl = ym + 1
        else:
            yr = ym - 1
    ans = min(ans,f(x,yl))

print(ans)