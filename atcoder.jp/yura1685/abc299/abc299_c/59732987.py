N = int(input())
S = str(input())
if '-' not in S:
    print(-1)
    exit()
S = list(map(str,S.split('-')))
ans = 0
for i in S:
    ans = max(ans,len(i))
print(ans if ans > 0 else -1)