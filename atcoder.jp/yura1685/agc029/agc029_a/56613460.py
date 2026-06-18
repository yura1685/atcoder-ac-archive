S = input()
if 'W' not in S or 'B' not in S:
    print(0)
    exit()
white_count = 0
ans = 0
for i in range(len(S)):
    if S[i] == 'W':
        white_count += 1
        ans += i + 1 - white_count
print(ans)