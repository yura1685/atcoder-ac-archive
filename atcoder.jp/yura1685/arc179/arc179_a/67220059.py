N, K = map(int,input().split())
A = list(map(int,input().split()))

if K >= 1:
    A.sort()
    print('Yes')
    print(*A)
if K <= 0 and sum(A) >= K:
    A.sort(reverse=True)
    print('Yes')
    print(*A)
if K <= 0 and sum(A) < K:
    print('No')