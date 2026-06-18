M, D = map(int,input().split())
ans = 0
for i in range(10,D+1):
    a, b = i//10, i%10
    if a >= 2 and b >= 2 and 1<= a*b <= M:
        ans += 1
print(ans)