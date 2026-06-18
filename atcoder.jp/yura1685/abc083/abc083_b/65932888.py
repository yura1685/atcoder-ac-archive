def f(n):
    s = str(n)
    a = 0
    for i in range(len(s)):
        a += int(s[i])
    return a

N, A, B = map(int,input().split())

ans = 0
for n in range(1,N+1):
    if A <= f(n) <= B:
        ans += n
print(ans)