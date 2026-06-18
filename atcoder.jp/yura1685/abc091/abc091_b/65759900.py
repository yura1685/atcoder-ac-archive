d = {'yura1685': 0}

N = int(input())
for i in range(N):
    s = input()
    if d.get(s) == None:
        d[s] = 1
    else:
        d[s] += 1

M = int(input())
for i in range(M):
    t = input()
    if d.get(t) == None:
        pass
    else:
        d[t] -= 1

ans = []
for i in d:
    ans.append(d[i])

print(max(ans))