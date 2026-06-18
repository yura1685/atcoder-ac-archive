N = int(input())

bal = [tuple(map(int,input().split())) for _ in range(N)]

def shot(X):
    a = [(X-bal[i][0])//(bal[i][1]) for i in range(N)]
    a.sort()
    c = [i <= a[i] for i in range(N)]
    if all(c):
        return True
    else:
        return False

l, r = 0, 10**20
while (r-l) > 1:
    mid = (r+l)//2
    if shot(mid):
        r = mid
    else:
        l = mid
print(r)