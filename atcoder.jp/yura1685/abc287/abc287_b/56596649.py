n, m = map(int,input().split())
S, T = [], []
for i in range(n):
    S.append(input())
for i in range(m):
    T.append(input())
ans = 0
for i in S:
    if i[3:] in T:
        ans += 1
print(ans)