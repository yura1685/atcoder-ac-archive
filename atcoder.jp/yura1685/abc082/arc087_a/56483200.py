from collections import Counter
n = int(input())
A = list(map(int,input().split()))
L = Counter(A)
ans = 0
for i in L:
    if L[i] < i:
        ans += L[i]
    elif L[i] > i:
        ans += L[i] - i
print(ans)