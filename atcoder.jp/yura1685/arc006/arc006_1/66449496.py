E = list(map(int,input().split()))
B = int(input())
L = list(map(int,input().split()))

ans = 0
for l in L:
    if l in E:
        ans += 1

if ans < 3:
    print(0)
elif 3 <= ans <= 4:
    print(8-ans)
elif ans == 6:
    print(1)
elif B in L:
    print(2)
else:
    print(3)