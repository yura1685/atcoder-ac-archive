S = input()

alp = [[] for _ in range(26)]

for i in range(len(S)):
    s = S[i]
    alp[ord(s)-ord('A')].append(i)

ans = 0
for x in alp:
    n = len(x)
    for i in range(1,n+1):
        ans += (-n+2*i-1)*x[i-1]
    ans -= n*(n-1)//2

print(ans)