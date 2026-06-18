from statistics import mode

N, M = map(int, input().split())
Terms = [[] for _ in range(N)]
Count = [0] * N
for _ in range(M):
    A, B, C = map(lambda x: int(x) - 1, input().split())
    Terms[C].append([A, B])

for c in range(N):
    if not Terms[c]: continue
    if len(Terms[c]) == 1:
        Terms[c] = [*Terms[c][0]]
        continue
    L = []
    for a, b in Terms[c]:
        L.append(a)
        L.append(b)
    m = mode(L)
    if L.count(m) < len(Terms[c]): ans = 0
    L2 = [m]
    for x in L:
        if x != m: L2.append(x)
    Terms[c] = L2

for c in range(N):
    if Terms[c]:
        for x in Terms[c]:
            Count[x] += 1
cnt0 = Count.count(0)

mod = 998244353
ans = 1
for c in reversed(range(N)):
    if Terms[c]:
        if len(Terms[c]) == 2:
            a, b = Terms[c]
            cnta, cntb = Count[a], Count[b]
            if cnta > 1 and cntb > 1:
                ans = 0
            elif cnta == 1 and cntb > 1:
                Count[b] -= 1
            elif cnta > 1 and cntb == 1:
                Count[a] -= 1
            else:
                ans = ans * 2 % mod
                cnt0 += 1
        else:
            m = Terms[c][0]
            cntm = Count[m]
            if cntm > 1:
                ans = 0
            else:
                for x in Terms[c][1:]:
                    Count[x] -= 1
                    if Count[x] == 0:
                        cnt0 += 1

    else:
        ans = ans * cnt0 % mod
        cnt0 -= 1

print(ans)