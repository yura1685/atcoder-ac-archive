S = input()
if S[0] != 'A':
    print('WA');exit()
if S[2:-1].count('C') != 1:
    print('WA');exit()
L = []
for i in S:
    if i == i.upper():
        L.append(i)
print('AC' if len(L) == 2 else 'WA')