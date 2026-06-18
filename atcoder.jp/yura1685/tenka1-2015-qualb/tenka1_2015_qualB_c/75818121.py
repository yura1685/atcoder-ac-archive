L = int(input())
mod = 10 ** 9 + 7
if L <= 6:
    print(0)
else:
    L -= 7
    u, d = L*L, 8
    if u % d == 0:
        print((u // 8) % mod)
    else:
        p = u // 8
        u %= 8
        print(p % mod if u <= 3 else (p+1) % mod)