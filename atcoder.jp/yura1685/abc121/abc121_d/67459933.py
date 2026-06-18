A, B = map(int,input().split())

def f(N):
    if N == -1:
        return 0
    gr = (N+1)//2
    m = (N+1) % 2
    r = N
    if gr % 2 == 0:
        if m == 0:
            return 0
        return r
    else:
        if m == 0:
            return 1
        r ^= 1
        return r
    
print(f(B)^f(A-1))