D = int(input())
N = int(input())
day = [0]*(D+1)
for _ in range(N):
    l, r = map(int,input().split())
    day[l-1] += 1
    day[r]   -= 1

for i in range(D):
    day[i+1] += day[i]
day.pop()
for d in day:
    print(d)