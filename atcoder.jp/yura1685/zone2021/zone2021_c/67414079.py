N = int(input())

Mem = [tuple(map(int,input().split())) for _ in range(N)]

def f(x): # xは可能か？
    p = [0]*32
    for i in range(N):
        c = '0b'+''.join(['1' if Mem[i][j] >= x else '0' for j in range(5)])
        p[int(c,2)] += 1
    for i in range(32):
        if p[i] == 0:
            continue
        for j in range(i,32):
            if p[j] == 0:
                continue
            if i == j and p[i] <= 1:
                    continue
            for k in range(j,32):
                if j == k and p[j] <= 1:
                    continue
                if i == j == k and p[i] <= 2:
                    continue
                if p[k] == 0:
                    continue
                if (i | j) | k == 31:
                    return True
    return False

l, r = 0, 10**9+1
while r - l > 1:
    mid = (l+r)//2
    if f(mid):
        l = mid
    else:
        r = mid

print(l)