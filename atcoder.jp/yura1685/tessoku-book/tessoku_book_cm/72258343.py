N, K = map(int,input().split())
A = list(map(int,input().split()))
X, Y = A[:N//2], A[N//2:]

def make(L):
    l = len(L)
    res = set()
    for n in range(1 << l):
        cnt = 0
        for i in range(l):
            if n >> i & 1:
                cnt += L[-1-i]
        res.add(cnt)
    return res

Z, W = make(X), make(Y)

for z in Z:
    if K - z in W:
        exit(print('Yes'))

print('No')