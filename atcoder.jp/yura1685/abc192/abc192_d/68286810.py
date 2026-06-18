X = input()
M = int(input())
N = len(X)

if N == 1:
    if int(X) <= M:
        print(1)
    else:
        print(0)
    exit()

def f(c):
    res = 0
    for i in range(N):
        res += int(X[-i-1])*c**i
        if res > M:
            return False
    return True

l, r = int(max(X)), 10**18+1

while r-l > 1:
    mid = (l+r)//2
    if f(mid):
        l = mid
    else:
        r = mid

print(l-int(max(X)))