N, M = map(int, input().split())
C = sorted(map(int, input().split()))
R = sorted(map(int, input().split()))
ans = 0
while R:
    r = R.pop()
    while C:
        c = C.pop()
        if c <= r:
            ans += 1
            break
print(ans)