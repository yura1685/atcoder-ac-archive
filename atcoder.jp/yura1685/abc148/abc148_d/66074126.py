N = int(input())
A = list(map(int,input().split()))

counter = 1
ans = 0
for a in A:
    if a == counter:
        counter += 1
        ans += 1
if ans == 0:
    print(-1)
else:
    print(N-ans)