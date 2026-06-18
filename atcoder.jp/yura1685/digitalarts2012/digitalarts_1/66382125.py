S = list(map(str,input().split()))
N = int(input())
ng = [[] for _ in range(21)]

def fil(a, b):
    n = len(a)
    for i in range(n):
        if b[i] != '*' and a[i] != b[i]:
            return False
    return True

for _ in range(N):
    t = input()
    ng[len(t)].append(t)

ans = []
for s in S:
    n = len(s)
    if n > 20:
        ans.append(s)
    elif ng[n]:
        for t in ng[n]:
            if fil(s,t):
                ans.append('*'*n)
                break
        else:
            ans.append(s)
    else:
        ans.append(s)
print(*ans)