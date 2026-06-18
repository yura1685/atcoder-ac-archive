n = int(input())
d = {}
for _ in range(n):
    s = input()
    if d.get(s) == None:
        d[s] = 1
    else:
        d[s] += 1

c = max(d.values())
for i in d:
    if d[i] == c:
        print(i)
        exit()