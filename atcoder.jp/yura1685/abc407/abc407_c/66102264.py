S = input()

n = len(S)
ans = 0
for i in range(n-1):
    l = int(S[i])
    r = int(S[i+1])
    if l-r >= 0:
        ans += l-r
    else:
        ans += 10+l-r
ans += int(S[-1]) + len(S)
print(ans)