S = input()
C = []
last = 'x'
cnt = 0
for s in S:
    if last == s:
        C.append(cnt)
        cnt = 1
    else:
        cnt += 1
    last = s
C.append(cnt)
ans = 0
for c in C:
    ans += c * (c+1) // 2

print(ans % 998244353)