S = input()
N = len(S)
ans = 0
for i in range(N):
    if S[i] != 'C':
        continue
    left = i
    right = N-i-1
    ans += min(left, right) + 1
print(ans)