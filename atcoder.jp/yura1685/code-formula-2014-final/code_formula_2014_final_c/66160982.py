S = list(map(str,input().split()))

ans = []
for s in S:
    if '@' in s:
        while s[0] != '@':
            s = s[1:]
        c = list(map(str,s.split('@')))
        for p in c:
            if p != '':
                ans.append(p)
ans = list(set(ans))
ans.sort()
for i in ans:
    print(i)