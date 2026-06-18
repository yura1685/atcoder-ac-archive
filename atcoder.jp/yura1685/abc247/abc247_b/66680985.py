N = int(input())
s, t = [], []
for _ in range(N):
    u, v = map(str,input().split())
    s.append(u)
    t.append(v)

for i in range(N):
    flag_s = False
    for S in [s[i],t[i]]:
        for j in range(N):
            if i == j:
                continue
            if S in [s[j],t[j]]:
                break
        else:
            flag_s = True
    if not flag_s:
        print('No')
        exit()

print('Yes')