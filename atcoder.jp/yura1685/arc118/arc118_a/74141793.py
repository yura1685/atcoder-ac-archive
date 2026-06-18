def tax(x): return (100+t)*x//100

t, N = map(int, input().split())

l, r = 0, 100*N
while r - l > 1:
    mid = (l + r) // 2
    if tax(mid) - mid < N:
        l = mid
    else:
        r = mid

print(tax(l) + 1)