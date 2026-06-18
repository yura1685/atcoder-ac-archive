def score(X):
    res = 0
    m = 0
    for x in X:
        if x == '(':
            res += 1
        else:
            res -= 1
        m = min(m, res)
    return m, res

N = int(input())
S = [score(input()) for _ in range(N)]
SP, SM = [], []
for s in S:
    if s[1] >= 0:
        SP.append(s)
    else:
        SM.append(s)
SP.sort(reverse=True)
SM.sort(key=lambda x: x[0] - x[1])

now = 0
for m, s in SP + SM:
    if now + m < 0: exit(print('No'))
    now += s 

print('Yes' if now == 0 else 'No')