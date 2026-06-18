K = int(input())
N = K
d = {}
for p in range(2,int(K**(1/2))+10):
    if K % p != 0:
        continue
    cnt = 0
    while K % p == 0:
        K //= p
        cnt += 1
    d[p] = cnt
if K != 1:
    d[K] = 1

def f(X):
    for p in d.keys():
        e = d[p]
        num = sum(X//(p**i) for i in range(1,41))
        if num < e:
            return False
    return True

l, r = 1, N+1
while r - l > 1:
    mid = (l+r)//2
    if f(mid):
        r = mid
    else:
        l = mid

print(r)