N = int(input())
C = sorted((int(x), i+1) for i, x in enumerate(input().split()))
pow = 2 ** N
S = set()

ans = 0
for c, n in C:
    if n not in S:
        ans += c
        S2 = set(s ^ n for s in S)
        for s in S2: S.add(s)
        S.add(n)
    if len(S) - (0 in S) == pow - 1:
        exit(print(ans))