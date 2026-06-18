N = int(input())
S = input()

ans = 0
for s in S:
    if s in 'ij':
        ans += 2
    else:
        ans += 1
print(ans)