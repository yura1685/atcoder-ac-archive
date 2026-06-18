S = list(input())
rev = False
fr, ba = [], []

Q = int(input())
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        rev = not rev
        continue
    if q[1] == '1':
        if rev:
            ba.append(q[2])
        else:
            fr.append(q[2])
    else:
        if rev:
            fr.append(q[2])
        else:
            ba.append(q[2])

if rev:
    print(''.join(ba[::-1] + S[::-1] + fr))
else:
    print(''.join(fr[::-1] + S + ba))