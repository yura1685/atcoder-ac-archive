def solve():
    a, b, c = map(int,input().split())
    a, c = min(a,c), max(a,c)
    if a <= b:
        print(a)
        return
    a, c = a-b, c-b
    x = c - a
    if x >= a:
        print(a+b)
        return 
    a -= x
    c -= 2*x
    print((a+c)//3+b+x)

T = int(input())
for _ in range(T):
    solve()