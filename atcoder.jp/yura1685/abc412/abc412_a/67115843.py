N = int(input())
ans = 0
for i in range(1,N+1):
    a, b = map(int,input().split())
    if a < b:
        ans += 1
print(ans)