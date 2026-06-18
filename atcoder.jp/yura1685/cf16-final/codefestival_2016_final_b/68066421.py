N = int(input())
s = set()

p = 0
i = 0
while p < N:
    i += 1
    p += i
    s.add(i)
if p > N:
    s -= set([p-N])

for i in s:
    print(i)