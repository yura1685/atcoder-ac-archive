N = int(input())
A = list(map(int, input().split()))

ok, ng = 0, max(A)+1
while ng - ok > 1:
    mid = (ok + ng) // 2
    X = [1 if a >= mid else 0 for a in A]
    for i in range(N-1):
        if X[N-1-i] == X[N-2-i] or X[N-1+i] == X[N+i]:
            ans = X[N-1-i]
            break
    else:
        ans = X[0]
    if ans == 1:
        ok = mid
    else:
        ng = mid

print(ok)