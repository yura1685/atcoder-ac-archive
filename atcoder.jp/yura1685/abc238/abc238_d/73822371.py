def solve():
    a, s = map(int,input().split())
    x = 0
    z = 0
    for bit in range(60):
        if (a >> bit) & 1:
            x |= 1 << bit
        else:
            z |= 1 << bit
    if 2 * x > s:
        print('No')
    else:
        w = s - 2 * x
        if w | z == z:
            print('Yes')
        else:
            print('No')

for _ in range(int(input())):
    solve()