N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

def f(x):
    res = 0
    for i in range(1, N+1):
        a = A[i]
        res += max(0, (x-a+i-1)//i)
    return res

ok, ng = 0, 10 ** 40
while ng - ok > 1:
    mid = (ng + ok) // 2
    if f(mid) <= K:
        ok = mid
    else:
        ng = mid

print(ok)