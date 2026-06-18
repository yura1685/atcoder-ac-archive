n = input()
ans = 0
for i in range(len(n)):
    ans += int(n[i])
print('Yes' if ans % 9 == 0 else 'No')