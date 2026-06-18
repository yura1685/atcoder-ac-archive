p = "ABCDE"
s = list(map(int, input().split()))
ans = []

for i in range(1, 6):
    if i == 1:
        for a in p:
            n = a
            sc = s[p.index(a)]
            ans.append((sc, n))
    elif i == 2:
        for a in p:
            for b in p:
                if b > a:
                    n = a + b
                    sc = s[p.index(a)] + s[p.index(b)]
                    ans.append((sc, n))
    elif i == 3:
        for a in p:
            for b in p:
                for c in p:
                    if b > a and c > b:
                        n = a + b + c
                        sc = s[p.index(a)] + s[p.index(b)] + s[p.index(c)]
                        ans.append((sc, n))
    elif i == 4:
        for a in p:
            for b in p:
                for c in p:
                    for d in p:
                        if b > a and c > b and d > c:
                            n = a + b + c + d
                            sc = s[p.index(a)] + s[p.index(b)] + s[p.index(c)] + s[p.index(d)]
                            ans.append((sc, n))
    elif i == 5:
        for a in p:
            for b in p:
                for c in p:
                    for d in p:
                        for e in p:
                            if b > a and c > b and d > c and e > d:
                                n = a + b + c + d + e
                                sc = s[p.index(a)] + s[p.index(b)] + s[p.index(c)] + s[p.index(d)] + s[p.index(e)]
                                ans.append((sc, n))

for i in range(len(ans)):
    for j in range(i + 1, len(ans)):
        if ans[i][0] < ans[j][0] or (ans[i][0] == ans[j][0] and ans[i][1] > ans[j][1]):
            ans[i], ans[j] = ans[j], ans[i]

for i in range(len(ans)):
    print(ans[i][1])
