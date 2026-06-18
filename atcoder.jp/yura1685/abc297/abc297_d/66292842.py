def f(a, b):
    if a < b:
        a, b = b, a
    if a > b:
        n = (a-b)//b
        c = n + (a%b != 0)
        a -= b*c
    return a, b, c

A, B = map(int,input().split())
ans = 0

while A != B:
    A, B, C = f(A,B)
    ans += C
print(ans)