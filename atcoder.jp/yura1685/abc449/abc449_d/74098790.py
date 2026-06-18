L, R, D, U = map(int, input().split())

def black(x, y):
    if y <= x:
        return y
    else:
        return x + (y-x)//2

def white(x, y):
    if y <= x:
        return 0
    else:
        return (y-x+1) // 2

ans = 0
for x in range(L, R+1):
    if x % 2 == 0:
        if U < 0:
            ans += black(abs(x), -D) - black(abs(x), -U-1)
        elif D <= 0 <= U:
            ans += black(abs(x), -D) + black(abs(x), U) + 1
        else:
            ans += black(abs(x), U) - black(abs(x), D-1)
    else:
        if U < 0:
            ans += white(abs(x), -D) - white(abs(x), -U-1)
        elif D <= 0 <= U:
            ans += white(abs(x), -D) + white(abs(x), U)
        else:
            ans += white(abs(x), U) - white(abs(x), D-1)

print(ans)