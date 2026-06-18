S = input()
T = input()

S2 = ''.join([s for s in S if s != 'A'])
T2 = ''.join([t for t in T if t != 'A'])

if S2 != T2:
    exit(print(-1))

def Count(X):
    counter = []
    cnt = 0
    for x in X:
        if x == 'A':
            cnt += 1
        else:
            counter.append(cnt)
            cnt = 0
    counter.append(cnt)
    return counter

Sc, Tc = Count(S), Count(T)
ans = 0
for i in range(len(Sc)):
    ans += abs(Sc[i] - Tc[i])

print(ans)