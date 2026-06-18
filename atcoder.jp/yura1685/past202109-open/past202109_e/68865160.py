N, K = map(int,input().split())
C = list(map(int,input().split()))
P = list(map(int,input().split()))
X = [(P[i],C[i]) for i in range(N)]
X.sort()

s = set()
pay = 0
cnt = 0

for p, c in X:
    if cnt == K:
        break
    if c in s:
        continue
    s.add(c)
    pay += p 
    cnt += 1

print(pay if cnt == K else -1)