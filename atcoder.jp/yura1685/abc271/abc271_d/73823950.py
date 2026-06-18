N, S = map(int,input().split())
ans = ['' for _ in range(S+1)]
dp = sorted([0])
for _ in range(N):
    a, b = map(int,input().split())
    dp2 = set()
    while dp:
        s = dp.pop()
        if s + a <= S:
            ans[s+a] = ans[s] + 'H'
            dp2.add(s+a)
        if s + b <= S :
            ans[s+b] = ans[s] + 'T'
            dp2.add(s+b)
        ans[s] = ''
    dp = sorted(dp2)

yn = ans[-1]
if yn:
    print('Yes')
    print(yn)
else:
    print('No')