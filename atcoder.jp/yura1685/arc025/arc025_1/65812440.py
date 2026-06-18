d = list(map(int,input().split()))
j = list(map(int,input().split()))
z = list(zip(d,j))
ans = 0
for i in z:
    ans += max(i)
print(ans)