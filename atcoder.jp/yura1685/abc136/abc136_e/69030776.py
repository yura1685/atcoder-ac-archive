from math import isqrt

N, K = map(int,input().split())
A = list(map(int,input().split()))
S = sum(A)

s = set()
for d in range(1,isqrt(S)+1):
    if S % d == 0:
        s.add(d)
        s.add(S//d)

ans = 1
for d in s:
    X = sorted(a % d for a in A if a % d > 0)
    n = len(X)
    if n == 0:
        ans = max(ans,d)
        continue

    fr = [0] + [x for x in X]
    ba = [d-x for x in X] + [0]
    
    for i in range(n):
        fr[i+1] += fr[i]
        ba[-i-2] += ba[-i-1]

    for i in range(n+1):
        f, b = fr[i], ba[i]
        if max(f,b) <= K:
            ans = max(ans,d)
            break

print(ans)