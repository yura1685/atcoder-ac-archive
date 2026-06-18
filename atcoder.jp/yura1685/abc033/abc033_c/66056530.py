S = input()
l = list(map(str,S.split('+')))

ans = 0
for i in l:
    if '0' not in i:
        ans += 1

print(ans)