N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

if Y < X:
    for i, a in enumerate(A):
        if a < Y: A[i] = -1
        elif a == Y: A[i] = 1
        elif Y < a < X: A[i] = 0
        elif a == X: A[i] = 2
        else: A[i] = -1
else:
    for i, a in enumerate(A):
        if a < X: A[i] = -1
        elif a == X: A[i] = 1
        else: A[i] = -1

def solve1(L):
    res = len(L) * (len(L) + 1) // 2
    cnt01, cnt02, cnt0 = 0, 0, 0
    for n in L:
        if n == 2:
            if cnt01:
                res -= cnt01 * (cnt01 + 1) // 2
                cnt01 = 0
            if cnt0:
                res += cnt0 * (cnt0 + 1) // 2
                cnt0 = 0
            cnt02 += 1
        if n == 1:
            if cnt02:
                res -= cnt02 * (cnt02 + 1) // 2
                cnt02 = 0
            if cnt0:
                res += cnt0 * (cnt0 + 1) // 2
                cnt0 = 0
            cnt01 += 1
        if n == 0:
            cnt01 += 1
            cnt02 += 1
            cnt0 += 1
    if cnt01:
        res -= cnt01 * (cnt01 + 1) // 2
    if cnt02:
        res -= cnt02 * (cnt02 + 1) // 2
    if cnt0:
        res += cnt0 * (cnt0 + 1) // 2
    
    return res

def solve2(L):
    res = 0
    cnt = 0
    for n in L:
        if n == 1:
            cnt += 1
        else:
            if cnt:
                res += cnt * (cnt + 1) // 2
                cnt = 0
    if cnt:
        res += cnt * (cnt + 1) // 2
    return res

LL = []
L = []
for n in A:
    if n != -1:
        L.append(n)
    else:
        if L:
            LL.append(L)
            L = []
if L:
    LL.append(L)

ans = 0
for L in LL:
    if Y < X:
        ans += solve1(L)
    else:
        ans += solve2(L)

print(ans)