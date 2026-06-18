N = int(input())
S = input() + 'X'
mod = 10**9 + 7
ans = []
cnt = 1
for i in range(N):
    if S[i] != S[i+1] and S[i+1] != 'X':
        cnt += 1
    elif S[i] == S[i+1]:
        ans.append(cnt)
        cnt = 1
    else:
        ans.append(cnt)

p = 1
for a in ans:
    p *= (a+1)//2
    p %= mod

print(p)