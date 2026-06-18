a, b = map(int,input().split())
d = abs(b-a)

ans = 0
ans += d//10
d %= 10
X = [0,1,2,3,2,1,2,3,3,2,1]
ans += X[d]
print(ans)