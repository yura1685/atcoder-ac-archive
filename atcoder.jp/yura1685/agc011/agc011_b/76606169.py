N = int(input())
A = sorted(map(int, input().split()))

ng, ok = -1, N - 1
while ok - ng > 1:
    flag = False
    mid = (ng + ok) // 2
    S = sum(A[:mid+1])
    for i in range(mid+1, N):
        a = A[i]
        if 2 * S >= a:
            S += a
        else:
            break
    else:
        flag = True
    if flag:
        ok = mid
    else:
        ng = mid

print(N - ok)