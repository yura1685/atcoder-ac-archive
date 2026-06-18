N, T = map(int,input().split())
A = list(map(int,input().split())) + [T]
A.reverse()

t = 0
ans = 0
while A:
    a = A.pop()
    if a < t:
        continue
    else:
        ans += (a-t)
        t = a + 100
print(ans)