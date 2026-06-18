H, W, K = map(int,input().split())

def solve(X, N:int) -> int:
    # xは含まれないものとしていい
    # 長さはK以上としてよい
    cnt = X[:K].count('o')
    res = K - cnt
    for i in range(N-K):
        if X[i] == 'o':
            cnt -= 1
        if X[K+i] == 'o':
            cnt += 1
        res = min(res, K-cnt)
    return res

ans = 10**8
S = [input() for _ in range(H)]
for s in S:
    for t in s.split('x'):
        N = len(t)
        if N < K:
            continue
        ans = min(ans, solve(t, N))

T = list(''.join(t) for t in zip(*S))
for t in T:
    for s in t.split('x'):
        N = len(s)
        if N < K:
            continue
        ans = min(ans, solve(s, N))

print(ans if ans < 10**8 else -1)