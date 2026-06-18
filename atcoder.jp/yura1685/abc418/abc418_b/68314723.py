S = input()
n = len(S)

ans = 0
for i in range(n-2):
    for j in range(i+3,n+1):
        t = S[i:j]
        if not t[0] == t[-1] == 't':
            continue
        ans = max(ans,(t.count('t')-2)/(len(t)-2))

print(ans)