from sortedcontainers import SortedList as S_L

N, M, Q = map(int, input().split())
n = N // 2
A = list(map(int, input().split()))
B = list(map(int, input().split()))
L = sorted(A + B)
SL, SM, SR = S_L(L[:n]), S_L(L[n:n+M]), S_L(L[n+M:])
ans = sum(SL) + sum(SR)

for _ in range(Q):
    t, i, new = map(int, input().split())
    if t == 1:
        old = A[i-1]
        A[i-1] = new
    else:
        old = B[i-1]
        B[i-1] = new
    
    if old in SL:
        SL.discard(old)
        ans -= old
        u = SM.pop(0)
        SL.add(u)
        ans += u
    elif old in SM:
        SM.discard(old)
    else:
        SR.discard(old)
        ans -= old
        u = SM.pop(M-1)
        SR.add(u)
        ans += u
    
    SM.add(new)
    if SL[n-1] > SM[0]:
        a, b = SL[n-1], SM[0]
        SL.discard(a)
        SL.add(b)
        SM.discard(b)
        SM.add(a)
        ans += b - a 
    
    if SM[M-1] > SR[0]:
        a, b = SR[0], SM[M-1]
        SR.discard(a)
        SR.add(b)
        SM.discard(b)
        SM.add(a)
        ans += b - a 
    
    print(ans)