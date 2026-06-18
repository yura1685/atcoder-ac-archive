n = int(input())

l, r = 0, n

if n in [1,2]:
    print(1)
    exit()
while r-l>1:
    mid = (r+l)//2
    if mid*(mid+1)//2 <= n+1:
        l = mid
    else:
        r = mid

print(n+1-l)