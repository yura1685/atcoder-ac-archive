S = input()
alp = 'abcdefghijklmnopqrstuvwxyz'

if len(S) < 26:
    for x in alp:
        if x not in S:
            S += x
            exit(print(S))

if S == alp[::-1]:
    exit(print(-1))

for i in range(25):
    if S[24-i] < S[25-i]:
        T = S[:24-i]
        U = S[24-i:]
        for x in alp:
            if x in U and U[0] < x:
                exit(print(T + x))