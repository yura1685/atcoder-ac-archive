n = int(input())
s = [input() for _ in range(n)]

alp = [[0]*(26) for _ in range(n)]
for i in range(n):
    x = s[i]
    for j in x:
        alp[i][ord(j)-ord('a')] += 1

z = list(zip(*alp))
ans = ''
for i in range(26):
    ans += chr(i+97)*min(z[i])

print(ans)