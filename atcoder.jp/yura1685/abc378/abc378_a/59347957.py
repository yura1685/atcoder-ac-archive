a = list(map(int,input().split()))
ans = 0
ans += a.count(1)//2
ans += a.count(2)//2
ans += a.count(3)//2
ans += a.count(4)//2
print(ans)