from bisect import bisect

Q = int(input())

flower = []
day = 0
ans = [0]

for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        flower.append(day)
    elif q[0] == 2:
        day += q[1]
    else:
        ans.append(bisect(flower,day-q[1]))

for i in range(len(ans)-1):
    print(ans[i+1]-ans[i])