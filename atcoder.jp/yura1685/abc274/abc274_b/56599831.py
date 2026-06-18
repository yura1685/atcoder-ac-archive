h, w = map(int,input().split())
glid = ['']*h
for i in range(h):
    glid[i] = list(input())

anslist = []
for i in range(w):
    ans = 0
    for j in range(h):
        if glid[j][i] == '#':
            ans += 1
    anslist.append(ans)
print(*anslist)