from bisect import bisect

N, K = map(int, input().split())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))

ng, ok = 0, A[-1] * B[-1] + 1
while ok - ng > 1:
    mid = (ng + ok) // 2
    cnt = 0
    for a in A:
        idx = bisect(B, mid // a)
        if idx == 0: break
        cnt += idx
    if cnt >= K:
        ok = mid
    else:
        ng = mid

print(ok)