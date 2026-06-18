N = int(input())
S = input().split('<')

ans = 0
for s in S:
    n = len(s)
    ans += n*(n+1)//2

print(ans)