from bisect import bisect

N, M = map(int, input().split())
S = input()
safe = [i for i, s in enumerate(S) if s == '0']

step = []
now = N
while True:
    if now <= M:
        step.append(now)
        break
    nex = now - M
    if S[nex] == '0':
        step.append(M)
        now = nex
    else:
        nex = safe[bisect(safe, nex)]
        if now == nex: exit(print(-1))
        step.append(now - nex)
        now = nex

step.reverse()
print(*step)