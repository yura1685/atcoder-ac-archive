N = int(input())
A = list(map(int,input().split()))

d = {}
ans = 0
for a in A:
    while a % 2 == 0:
        a //= 2
    if d.get(a) == None:
        d[a] = 1
        ans += 1

print(ans)