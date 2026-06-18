s = input()
d = set(s)
if len(d) == 2 and s.count(s[0]) == 2:
    print('Yes')
else:
    print('No')