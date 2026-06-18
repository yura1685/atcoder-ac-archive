N = int(input())
ans = []
d = {}
for _ in range(N):
    s = input()
    t = list(s)
    t = reversed(t)
    m = ''.join(t)
    d[m] = s 
    ans.append(m)
ans.sort()
for i in ans:
    print(d[i])