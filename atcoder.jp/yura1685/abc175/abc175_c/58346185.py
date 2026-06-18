x, k, d = map(int,input().split())
x = abs(x)
if x - k*d >= d:
    print(x-k*d)
    exit()
if x % d == 0:
    t = x // d
    if t % 2 == k % 2:
        print(0)
    else:
        print(d)
    exit()
t = x // d
if t % 2 == k % 2:
    print(x-d*t)
else:
    print(abs(x-d*t-d))