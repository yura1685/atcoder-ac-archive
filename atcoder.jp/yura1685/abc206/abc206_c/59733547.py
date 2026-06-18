from collections import Counter

def p(n):
    return n*(n-1)//2

N = int(input())
A = list(map(int,input().split()))

c, C = Counter(A), set(A)

ans = p(N)
for i in C:
    ans -= p(c[i])

print(ans)