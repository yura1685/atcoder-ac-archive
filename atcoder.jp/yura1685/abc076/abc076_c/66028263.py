def f(a,b):
    for i in range(len(a)):
        if a[i] != '?' and a[i] != b[i]:
            return False
    return True

s = input()
t = input()

k = len(s)-len(t) + 1

ansl = []
for i in range(k):
    x = s[i:i+len(t)]
    if f(x,t):
        y = list(s)
        y[i:i+len(t)] = t
        ans = ''
        for j in y:
            if j != '?':
                ans += j
            else:
                ans += 'a'
        ansl.append(ans)
ansl.sort()
if ansl == []:
    print('UNRESTORABLE')
else:
    print(ansl[0])