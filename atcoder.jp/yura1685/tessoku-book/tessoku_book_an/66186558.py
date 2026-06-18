from collections import Counter

def f(n):
    return n*(n-1)*(n-2)//6

n = int(input())
a = list(map(int,input().split()))

c = Counter(a)
ans = 0
for x in c.values():
    ans += f(x)

print(ans)