L, R = map(int,input().split())
l = list(map(int,input().split()))
r = list(map(int,input().split()))
counter = 0
ans = 0
while True:
    if counter >= len(l):
        break
    a = l[counter]
    if a in r:
        r.remove(a)
        l.remove(a)
        ans += 1
    else:
        counter += 1
print(ans)