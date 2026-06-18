N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

s1, s2 = set(), set()
for a in A:
    for b in B:
        s1.add(a+b)
for c in C:
    for d in D:
        s2.add(c+d)

for n in s1:
    if K - n in s2:
        print('Yes')
        break
else:
    print('No')