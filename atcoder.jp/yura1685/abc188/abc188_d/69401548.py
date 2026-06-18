N, C = map(int,input().split())

E = []
for _ in range(N):
    a, b, c = map(int,input().split())
    E.append((a,1,c))
    E.append((b+1,-1,c))
E.sort()

ans = 0
now = 0
last = E[0][0]

for day, act, pri in E:
    if day > last:
        ans += (day - last) * min(C, now)
    now += pri * act
    last = day

print(ans)