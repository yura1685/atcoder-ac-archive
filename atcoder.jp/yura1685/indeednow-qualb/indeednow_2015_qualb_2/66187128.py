s = input()
t = input()
if len(s) != len(t):
    print(-1)
    exit()
if s == t:
    print(0)
    exit()
n = len(s)
for i in range(n):
    s = s[-1] + s[:-1]
    if s == t:
        print(i+1)
        exit()
print(-1)