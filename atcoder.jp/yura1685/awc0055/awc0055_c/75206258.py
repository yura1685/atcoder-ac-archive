N = int(input())
W = sorted(map(int, input().split()))
C = sorted(map(int, input().split()), reverse=True)
ans = 0
for w in W:
    while C:
        if w <= C.pop():
            ans += 1
            break
print(ans)