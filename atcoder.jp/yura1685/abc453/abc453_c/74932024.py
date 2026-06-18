N = int(input())
L = [2*int(x) for x in input().split()]
def f(x, y):
    if (x < 0 and y > 0) or (x > 0 and y < 0):
        return True
    return False

ans = 0
for bit in range(1 << N):
    cnt = 0
    now = 1
    for k in range(N):
        if (bit >> k) & 1:
            cnt += f(now, now + L[k])
            now += L[k]
        else:
            cnt += f(now, now - L[k])
            now -= L[k]
    ans = max(ans, cnt)

print(ans)