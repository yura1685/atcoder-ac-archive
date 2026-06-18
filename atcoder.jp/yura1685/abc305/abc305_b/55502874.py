p, q = map(str,input().split())
x = [0,3,4,8,9,14,23]
y = ['A','B','C','D','E','F','G']
a, b = y.index(p), y.index(q)
s, t = x[a], x[b]
print(abs(s-t))