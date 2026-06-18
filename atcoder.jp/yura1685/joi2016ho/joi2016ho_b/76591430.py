from itertools import accumulate

N = int(input())
S = list(input())

ans1 = 0
cj, co = 1, 0
for s in S:
    if s == 'J':
        cj += 1
    elif s == 'O':
        co += cj
    else:
        ans1 += co

T = list(reversed(S))
ans2 = 0
ci, co = 1, 0
for t in T:
    if t == 'I':
        ci += 1
    elif t == 'O':
        co += ci
    else:
        ans2 += co

LJ, LI = [0] * N, [0] * N
for i, s in enumerate(S):
    if s == 'J':
        LJ[i] = 1
for i, t in enumerate(T):
    if t == 'I':
        LI[i] = 1

LJ, LI = list(accumulate(LJ)), list(accumulate(LI))
LI.reverse()

ans3, M = 0, 0
for i, s in enumerate(S):
    if i + 1 < N:
        c = LJ[i] * LI[i+1]
        if s == 'O':
            ans3 += c
        M = max(M, c)
ans3 += M

print(max(ans1, ans2, ans3))