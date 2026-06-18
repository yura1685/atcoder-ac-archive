S = input()
n = len(S)
ans = 0
for i in range(n):
    s = S[i]
    if s == 'U':
        ans += 2*i + (n-i-1)
    else:
        ans += 2*(n-i-1) + i

print(ans)