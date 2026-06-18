import sympy

N = int(input())
d = sum((sympy.factorint(N)).values())

ans = 0
while d != 1:
    d = (d+1)//2
    ans += 1

print(ans)