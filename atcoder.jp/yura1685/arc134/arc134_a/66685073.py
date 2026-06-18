N, L, W = map(int,input().split())
A = list(map(int, input().split()))

nosheet = []
last = 0
for a in A:
    if last >= L:
        break
    if a <= last:
        last = a+W
    else:
        nosheet.append(a-last)
        last = a+W
if last < L:
    nosheet.append(L-last)

ans = 0
for i in range(len(nosheet)):
    ans += (nosheet[i]+W-1)//W

print(ans)