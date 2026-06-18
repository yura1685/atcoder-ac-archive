N = int(input())
A = list(map(int,input().split()))
cut = [0]
now = 0
for a in A:
    now = (now+a) % 360
    cut.append(now)
cut.append(360)
cut.sort()

m = 0
for i in range(N+1):
    m = max(cut[i+1]-cut[i], m)

print(m)