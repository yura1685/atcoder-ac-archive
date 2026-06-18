from bisect import bisect_left as b_l, bisect_right as b_r

N, K = map(int, input().split())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()

def f(A, t) -> int:
    low, high = A[0] - t, A[-1]
    res = high
    while high - low > 1:
        mid = (low + high) // 2
        l_cnt = b_r(A, mid)
        r_cnt = N - b_l(A, mid+t+1)
        if l_cnt - r_cnt >= 0:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res

def g(A, l, t):
    res = 0
    for a in A:
        if a < l:
            res += l - a 
        elif a > l + t:
            res += a - l - t
    return res

ng, ok = -1, 1 << 30
while ok - ng > 1:
    mid = (ng + ok) // 2
    lx = f(X, mid)
    ly = f(Y, mid)
    if g(X, lx, mid) + g(Y, ly, mid) <= K:
        ok = mid
    else:
        ng = mid

print(ok)