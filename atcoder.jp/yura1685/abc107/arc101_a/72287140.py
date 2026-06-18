N, K = map(int,input().split())
X = list(map(int,input().split()))
M, P = [], []
for x in X:
    if x < 0: M.append(-x)
    elif x > 0: P.append(x)
    else: K -= 1

M.reverse()

ans = 10**10
for i in range(max(0, K-len(P)), min(len(M),K)+1):
    m = M[i-1] if i else 0
    p = P[K-i-1] if K-i else 0
    ans = min(ans, 2*m+p, m+2*p)

print(ans)