def solve():
    a, b, c = map(int,input().split())
    if (a+b+c) % 3 == 0 and (a-b) % 2 == (b-c) % 2:
        mid = (a+b+c)//3
        if mid % 2 == a % 2:
            d = [abs(a-mid),abs(b-mid),abs(c-mid)]
            print(sum(d)//4)
        else:
            print(-1)
    else:
        print(-1)

T = int(input())
for _ in range(T):
    solve()