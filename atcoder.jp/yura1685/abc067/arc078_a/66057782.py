N = int(input())
a = list(map(int,input().split()))

ans = 10**20
S = sum(a)
s = 0
for i in range(0,N-1):
    s += a[i]
    ans = min(ans, abs(S-2*s))
print(ans)