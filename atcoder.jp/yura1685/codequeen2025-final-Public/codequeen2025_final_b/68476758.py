from collections import Counter

N, S = map(int,input().split())
A = list(map(int,input().split()))
C = Counter(A)
s = set(A)

ans = 0

for a in A:
    if 2 * a >= S:
        continue
    if S - a in s:
        ans += C[S-a]

if S % 2 == 0:
    ans += C[S//2] * (C[S//2]-1) // 2

print(ans)