N = int(input())

def f(x):
    return x**3 + x

l, r = 0, N
while abs(f(r)-N) > 10**-8:
    mid = (l+r)/2
    if f(mid) > N:
        r = mid
    else:
        l = mid

print(r)