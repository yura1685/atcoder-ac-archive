h, w = map(int,input().split())
s = ['']*h
for i in range(h):
    s[i] = list(map(int,input().split()))
t = [i for i in zip(*s)]
for i in range(w):
    print(*t[i])