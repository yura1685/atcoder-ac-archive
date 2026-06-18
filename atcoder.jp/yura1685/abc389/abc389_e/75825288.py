N, M = map(int, input().split())
P = sorted(map(int, input().split()))

def solve(X):
    res = 0
    for p in P:
        k = ((X // p) + 1) // 2
        res += k * k * p
    return res

l, r = 0, 10 ** 30
while r - l > 1:
    mid = (l + r) // 2
    cnt = solve(mid)
    if cnt > M:
        r = mid
    else:
        l = mid

ans = 0
money = M
for p in P:
    k = ((l // p) + 1) // 2
    ans += k
    money -= k * k * p

for p in P:
    k = ((l // p) + 1) // 2
    nex = (2 * k + 1) * p
    if nex == r and money >= nex:
        ans += 1
        money -= nex

print(ans)