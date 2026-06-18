n = int(input())
right, left = 0, 0
l,r = 0, 0
hirou = 0
for i in range(n):
    a, s = map(str,input().split())
    a = int(a)
    if s == 'L' and l == 0:
        left = a
        l += 1
    if s == 'R' and r == 0:
        right = a
        r += 1
    elif s == 'L':
        hirou += abs(left-a)
        left = a
    elif s == 'R':
        hirou += abs(right-a)
        right = a
print(hirou)