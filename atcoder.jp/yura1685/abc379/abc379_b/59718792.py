N, K = map(int,input().split())
S = list(map(str,input().split('X')))
ans = 0
for i in S:
    ans += len(i)//K

print(ans)