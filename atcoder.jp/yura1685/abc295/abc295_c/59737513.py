from collections import Counter

N = int(input())
A = list(map(int,input().split()))
c, d = Counter(A), set(A)

ans = 0
for i in d:
    ans += c[i]//2
print(ans)