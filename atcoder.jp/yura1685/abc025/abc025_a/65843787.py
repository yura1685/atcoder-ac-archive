S = input()
N = int(input())
c = []
for i in S:
    for j in S:
        x = i+j
        c.append(x)
c.sort()
print(c[N-1])