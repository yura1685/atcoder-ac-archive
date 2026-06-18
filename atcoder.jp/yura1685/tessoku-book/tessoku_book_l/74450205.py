N, K = map(int, input().split())
A = list(map(int, input().split()))
ng, ok = 0, min(A) * K
while ok - ng > 1:
    mid = (ng + ok) // 2
    paper = sum(mid // a for a in A)
    if paper < K:
        ng = mid
    else:
        ok = mid

print(ok)