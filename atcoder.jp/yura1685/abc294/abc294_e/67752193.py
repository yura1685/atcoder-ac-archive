L, N1, N2 = map(int,input().split())

A = [tuple(map(int,input().split())) for _ in range(N1)]
B = [tuple(map(int,input().split())) for _ in range(N2)]

na, la = 0, 0
nb, lb = 0, 0
ia, ib = -1, -1
ans = 0
while not (la == lb == L):
    if la == lb:
        ia, ib = ia+1, ib+1
        na, la2 = A[ia]
        nb, lb2 = B[ib]
        if na == nb:
            ans += min(la2,lb2)
        la += la2
        lb += lb2
    elif la > lb:
        ib += 1
        nb, lb2 = B[ib]
        if na == nb:
            ans += min(la-lb,lb2)
        lb += lb2
    elif la < lb:
        ia += 1
        na, la2 = A[ia]
        if na == nb:
            ans += min(lb-la,la2)
        la += la2

print(ans)