from collections import Counter

N = int(input())
A = list(map(int,input().split()))
B = [0]
s = 0
for i in range(N):
    s += A[i]
    B.append(s)

v = Counter(B).values()

ans = 0
for n in v:
    ans += n*(n-1)//2
  
print(ans)