N = int(input())
s = set()
for _ in range(N):
    S, E = input().split('-')
    SH, SM = int(S[:2]), int(S[2:])
    EH, EM = int(E[:2]), int(E[2:])
    SM = (SM // 5) * 5
    EM = ((EM+4)//5) * 5
    if EM == 60:
        EH += 1
        EM = 0
    s.add((60*SH+SM, 60*EH+EM))

L = sorted(s)

ans = []

s, e = L[0]
for i in range(len(L)):
    ns, ne = L[i]
    if s <= ns <= e:
        e = max(e,ne)
    else:
        ans.append((s,e))
        s, e = ns, ne

if not ans or ans[-1] != (s,e):
    ans.append((s,e))

for s, e in ans:
    x = str((s//60)*100 + s % 60)
    y = str((e//60)*100 + e % 60)
    x = '0'*(4-len(x)) + x
    y = '0'*(4-len(y)) + y
    print(x+'-'+y)