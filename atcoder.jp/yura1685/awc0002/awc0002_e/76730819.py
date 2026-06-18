from collections import Counter

N, S = map(int, input().split())
A = list(map(int, input().split()))

def f(L):
    res = []
    for bit in range(1 << len(L)):
        s = 0
        for i in range(len(L)):
            if (bit >> i) & 1:
                s += L[i]
        res.append(s)
    return res

X, Y = Counter(f(A[:N//2])), f(A[N//2:])
ans = 0
for y in Y:
    if S - y in X:
        ans += X[S-y]
print(ans)