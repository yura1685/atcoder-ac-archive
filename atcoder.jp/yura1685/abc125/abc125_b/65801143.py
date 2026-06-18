N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))
ans = 0
X = zip(V,C)
for i in X:
    ans += max(i[0]-i[1], 0)
print(ans)