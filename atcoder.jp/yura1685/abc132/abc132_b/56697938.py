ans = 0
n = int(input())
p = list(map(int,input().split()))
for i in range(n-2):
    a, b, c = p[i], p[i+1], p[i+2]
    if a+b+c - max(a,b,c) - min(a,b,c) == b:
        ans += 1
print(ans)