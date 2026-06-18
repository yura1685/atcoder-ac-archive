N = int(input())
H = list(map(int, input().split()))

s = []
ans = []
for h in H[::-1]:
    ans.append(len(s))
    while s != [] and s[-1] < h:
        s.pop()
    s.append(h)

print(*ans[::-1])