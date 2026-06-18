N = int(input())
H = list(map(int, input().split()))
M = 0
ans = 0
for h in H:
    if M < h:
        ans += 1
        M = h
print(ans)