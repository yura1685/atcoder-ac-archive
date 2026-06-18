N = int(input())
A = list(map(int,input().split()))

s = 0
s_max = 0
now = 0
ans = 0

for i in range(N):
    a = A[i]
    ans = max(ans,now+s_max)
    now += s + a
    s += a
    s_max = max(s,s_max)
    ans = max(ans,now)

print(ans)