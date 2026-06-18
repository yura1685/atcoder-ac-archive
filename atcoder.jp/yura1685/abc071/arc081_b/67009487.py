N = int(input())
S = input()
T = input()
mod = 10**9 + 7

if S[0] == T[0]:
    ans = 3
    cnt = 1
    l = 0
else:
    ans = 6
    cnt = 2
    l = 1

while cnt < N:
    if S[cnt] == T[cnt]:
        if l == 0:
            ans *= 2
        l = 0
        cnt += 1
    else:
        if l == 0:
            ans *= 2
        else:
            ans *= 3
        l = 1
        cnt += 2
    ans %= mod

print(ans)