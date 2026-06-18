N, K = map(int, input().split())
A = list(map(int, input().split()))
ok, ng = 0, sum(A) + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    lst = []
    s = 0
    for a in A:
        s += a
        if s >= mid:
            lst.append(s)
            s = 0
    if len(lst) >= K:
        ok = mid
    else:
        ng = mid

print(ok)