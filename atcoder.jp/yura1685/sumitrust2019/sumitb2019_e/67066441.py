N = int(input())
A = list(map(int,input().split()))
mod = 10**9+7

ans = 1
cnt = [0,0,0]

for a in A:
    c = cnt.count(a)
    ans = ans*c%mod
    if c == 0:
        ans = 0
        break
    cnt[cnt.index(a)] += 1

print(ans)