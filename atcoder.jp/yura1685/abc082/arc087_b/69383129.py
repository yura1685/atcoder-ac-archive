from more_itertools import run_length

S = input()
S = list(run_length.encode(S))
x, y = map(int,input().split())

yoko = []
tate = []

if S[0][0] == 'F':
    x -= S[0][1]
    S.pop(0)

dic = {'x':'y', 'y':'x'}
d = 'x'
for s in S:
    if s[0] == 'T':
        if s[1] % 2 == 1:
            d = dic[d]
    else:
        if d == 'x':
            yoko.append(s[1])
        else:
            tate.append(s[1])

def f(A,N):
    if not A:
        return N == 0
    S_total = sum(A)
    if (N + S_total) % 2 == 1:
        return False
    if N < 0:
        N = -N
    if N > S_total:
        return False
    p = 2*S_total + 3
    dp = [[False] * p for _ in range(len(A) + 1)]
    dp[0][S_total+1] = True

    for i in range(len(A)):
        a = A[i]
        for j in range(p):
            if dp[i][j]:
                dp[i+1][j+a] = True
                dp[i+1][j-a] = True

    return dp[-1][S_total+1+N]

if f(yoko,x) and f(tate,y):
    print('Yes')
else:
    print('No')