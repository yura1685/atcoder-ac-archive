from math import ceil

c = []
for _ in range(5):
    c.append(int(input()))

d = [(i-1) % 10 + 1 for i in c]
e = [10*ceil(i/10) for i in c]

print(sum(e)-10+min(d))