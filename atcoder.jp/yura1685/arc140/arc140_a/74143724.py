from collections import Counter
def f(X:str) -> int:
    C = Counter(X)
    return len(X) - max(C.values())
N, K = map(int, input().split())
S = input()
ans = N
for d in range(1, N+1):
    if N % d: continue
    cnt = 0
    for i in range(d):
        cnt += f(S[i::d])
        if cnt > K: break
    else: exit(print(d))