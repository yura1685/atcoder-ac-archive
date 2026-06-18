N = int(input())
S = [input() for _ in range(N)]

BA, A, B, X = 0, 0, 0, 0
for s in S:
    if s[0] == 'B':
        if s[-1] == 'A':
            BA += 1
        else:
            B += 1
    else:
        if s[-1] == 'A':
            A += 1
        else:
            X += 1

cnt = 0

if A > 0:
    A -= 1
    cnt += BA
    BA = 0
    if B > 0:
        B -= 1
        cnt += 1
    cnt += min(A,B)

else:
    if BA > 0:
        cnt += BA - 1
        if B > 0:
            cnt += 1

for s in S:
    cnt += s.count('AB')

print(cnt)